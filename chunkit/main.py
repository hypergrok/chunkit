import requests


class Chunker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://app.chunkit.dev/api/v1/chunk"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def process(self, urls):
        if isinstance(urls, str):
            urls = [urls]
        elif not isinstance(urls, list):
            raise ValueError("URLs should be provided as a string, or list of strings for batch mode.")

        data = {'urls': urls}
        response = requests.post(self.endpoint, json=data, headers=self.headers)

        if response.status_code != 200:
            response.raise_for_status()

        return response.json().get('chunkified_urls', [])
