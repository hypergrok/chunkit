import requests
import html2text
from bs4 import BeautifulSoup
import hashlib
import platform
import uuid
import toml
import os
import re
import traceback
import mimetypes
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from collections import Counter


class Chunker:
    def __init__(self, api_key=None):
        project_root_config = os.path.join(os.getcwd(), "config.toml")
        package_default_config = os.path.join(os.path.dirname(__file__), "config.toml")

        if os.path.exists(project_root_config):
            self.config = toml.load(project_root_config)
        else:
            self.config = toml.load(package_default_config)
        # optional anonymized usage stats
        self.session_id = self.get_session_id() if self.config['settings']['gather_usage_stats'] else 'no_sessionid'
        self.api_key = api_key  # For developers who want more functionality than Core mode
        self.endpoint = "https://app.chunkit.dev/api/v1/chunk"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.core_mode = False if self.api_key else True
        self.local_only_mode = self.config['settings']['local_only_mode']

    @staticmethod
    def split_into_chunks(markdown):
        if markdown == "" or markdown is None:
            return []
        headers = re.findall(r'^(#{1,5})\s', markdown, re.MULTILINE)
        if len(headers) < 1:
            print("Warning: Could not find well-formatted markdown headers - returning full markdown")
            return [markdown]
        most_common_header = Counter(headers).most_common(1)[0][0]
        chunks = re.split(rf'(?=^{most_common_header}\s)', markdown, flags=re.MULTILINE)
        if chunks[0].strip() == '':
            chunks.pop(0)
        return chunks

    def get_chunks(self, urls):
        chunkified_urls = []
        for url in urls:
            chunk_obj = {}
            try:
                url_path = urlparse(url).path
                ext, ctype = os.path.splitext(url_path)[1], mimetypes.guess_type(url_path)[0]
                if ctype is None or ext.startswith(".htm"):  # Fallback
                    ctype = "text/html"
                if "html" not in ctype:
                    err = ("Only HTML is supported with Chunkit Core. For other filetypes,"
                           " you can get an API key for Chunkit Plus: app.chunkit.dev")
                    raise ValueError(err)
                body = urlopen(Request(url=url)).read().decode(errors="ignore")
                soup = BeautifulSoup(body, 'html.parser')
                heading = soup.title.string if soup.title else ""
                params = {'ignore_links': True, 'body_width': 0, 'ignore_images': True, 'inline_links': True}
                txt_handler = html2text.HTML2Text()
                for key, value in params.items():
                    setattr(txt_handler, key, value)
                markdown = txt_handler.handle(str(soup))
                chunks = self.split_into_chunks(markdown)
                chunk_obj = {
                    'heading': heading,
                    'url': url,
                    'success': True,
                    'error': {},
                    'chunks': chunks
                }
            except Exception as e:
                if self.config['settings'].get('verbose', False):
                    print(traceback.format_exc())
                errobj = {"message": str(e), "type": type(e).__name__}
                chunk_obj = {'heading': "", 'url': url, 'success': False, "error": errobj}
            finally:
                chunkified_urls.append(chunk_obj)
        return chunkified_urls

    def process(self, urls):
        if isinstance(urls, str):
            urls = [urls]
        elif not isinstance(urls, list):
            raise ValueError("URLs should be provided as a string, or list of strings for batch mode.")

        if self.local_only_mode:
            chunks = self.get_chunks(urls)
        else:
            determined_headers = {} if self.core_mode else self.headers
            data = {'urls': urls, 'session_id': self.session_id}
            response = requests.post(self.endpoint, json=data, headers=determined_headers)

            if response.status_code != 200:
                response.raise_for_status()

            chunks = response.json().get('chunkified_urls', [])
        for item in chunks:
            print(f"Chunking for url {item['url']} successful: {item['success']}")
        return chunks

    @staticmethod
    def get_session_id():
        # Anonymized but semi-persistent info
        persistent_info = (platform.system(), platform.machine(), platform.processor(), uuid.getnode())
        unique_string = ''.join(map(str, persistent_info))
        anonymous_session_id = hashlib.sha256(unique_string.encode()).hexdigest()
        return anonymous_session_id
