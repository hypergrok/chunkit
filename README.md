# chunkit

<p align="center">
  <img src="chn.png" alt="chunkit" width="200" style="filter: invert(100%) brightness(0.8);"/>
</p>

[![PyPI version](https://badge.fury.io/py/chunkit.svg)](https://badge.fury.io/py/chunkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/chunkit)](https://pepy.tech/project/chunkit)

## Convert URLs and files into LLM-friendly markdown chunks

chunkit transforms URLs into clean markdown chunks which can be used for RAG/LLM applications.

## Features

- **Easy to Use**: Simple API to convert URLs and files into markdown chunks.
- **Fast and Efficient**: Optimized for performance.
- **LLM-Friendly**: Produces chunks that are ideal for LLM processing.
- **File Support**: Handles HTML, PDF, CSV, JSON, YAML, MD, DOCX.

## Installation

Install chunkit using pip:

```bash
pip install chunkit
```

## Quick Start

Get started with chunkit in a few lines of code:

```python
from chunkit import Chunker

# Initialize the Chunker with your API key
chunker = Chunker(api_key='your_api_key_here')

# Define URLs to process
urls = ["https://lol.com", "https://calibre-ebook.com/downloads/demos/demo.docx"]

# Process the URLs into semantic embedding chunks
chunks = chunker.process(urls)

# Output the resulting chunks
for chunk in chunks:
    print(chunk)
```

## Getting an API Key

To use chunkit, you need an API key:

1. Go to [app.chunkit.dev](https://app.chunkit.dev).
2. Sign up or log in to your account. 
3. Navigate to Deploy API section.
4. Generate a new API key.

You can also test chunking directly on the website.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue or contact us at support@chunkit.dev.

---

Happy chunking!