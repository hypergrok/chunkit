import requests
import html2text
from bs4 import BeautifulSoup
import hashlib
import platform
import uuid
import toml


class Chunker:
    def __init__(self, api_key=None):
        self.api_key = api_key  # Used only for Plus mode
        self.endpoint = "https://app.chunkit.dev/api/v1/chunk"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.config = toml.load("./config.toml")
        # optional anonymized usage stats
        self.fingerprint = self.get_fingerprint() if self.config['settings']['gather_usage_stats'] else 'anonymous'

    def process(self, urls):
        if isinstance(urls, str):
            urls = [urls]
        elif not isinstance(urls, list):
            raise ValueError("URLs should be provided as a string, or list of strings for batch mode.")

        core_mode = False if self.api_key else True
        local_only_mode = self.config['settings']['local_only_mode']

        if core_mode or local_only_mode:
            html_body = "placeholder"
            soup = BeautifulSoup(html_body, "html.parser")
            params = {
                'ignore_links': True,
                'body_width': 0,
                'ignore_images': True,
                'inline_links': True,
            }
            txt_handler = html2text.HTML2Text()
            for key, value in params.items():
                setattr(txt_handler, key, value)
            markdown = txt_handler.handle(str(soup))
        else:
            data = {'urls': urls, 'session_id': self.fingerprint}
            response = requests.post(self.endpoint, json=data, headers=self.headers)

            if response.status_code != 200:
                response.raise_for_status()

            return response.json().get('chunkified_urls', [])

    @staticmethod
    def get_fingerprint():
        stable_info = (
            platform.system(),
            platform.machine(),
            platform.processor(),
            uuid.getnode()
        )
        unique_string = ''.join(map(str, stable_info))
        fingerprint = hashlib.sha256(unique_string.encode()).hexdigest()
        return fingerprint
