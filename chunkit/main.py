import requests
import html2text
from bs4 import BeautifulSoup


class Chunker:
    def __init__(self, api_key=None):
        self.api_key = api_key  # Used only for Plus mode
        self.endpoint = "https://app.chunkit.dev/api/v1/chunk"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def process(self, urls):
        if isinstance(urls, str):
            urls = [urls]
        elif not isinstance(urls, list):
            raise ValueError("URLs should be provided as a string, or list of strings for batch mode.")

        core_mode = False if self.api_key else True

        if core_mode:
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
            data = {'urls': urls}
            response = requests.post(self.endpoint, json=data, headers=self.headers)

            if response.status_code != 200:
                response.raise_for_status()

            return response.json().get('chunkified_urls', [])
