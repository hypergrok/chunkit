<p align="center">
  <img src="chn.png" alt="chunkit" width="200"/>
</p>

<div align="center">
  <a href="https://badge.fury.io/py/chunkit"><img src="https://badge.fury.io/py/chunkit.svg" alt="PyPI version" /></a>
  <a href="https://pepy.tech/project/chunkit"><img src="https://pepy.tech/badge/chunkit" alt="Downloads" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
</div>

### Turn URLs into LLM-friendly markdown chunks

chunkit transforms URLs into markdown chunks which can be used for RAG/LLM applications.

### Installation

Install chunkit using pip:

```bash
pip install chunkit
```

Start chunking:

```python
from chunkit import Chunker

# Initialize the Chunker with your API key
chunker = Chunker(api_key='your_api_key_here')

# Define URLs to process
urls = ["https://en.wikipedia.org/wiki/Chunking", "https://calibre-ebook.com/downloads/demos/demo.docx"]

# Process the URLs into markdown chunks
chunks = chunker.process(urls)

# Output the resulting chunks
for chunk in chunks:
    print(chunk)
```

### Get API Key

1. Go to [app.chunkit.dev](https://app.chunkit.dev).
2. Sign up or log in to your account. 
3. Navigate to Deploy API section.
4. Generate a new API key.

You can also test chunking directly on the website.

### Supported files

Handles HTML, PDF, CSV, JSON, YAML, MD, DOCX.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For questions or support, please open an issue.