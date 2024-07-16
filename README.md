<p align="center">
  <img src="https://raw.githubusercontent.com/hypergrok/chunkit/main/chn.png" alt="chunkit" width="200"/>
</p>

<div align="center">
  <a href="https://badge.fury.io/py/chunkit"><img src="https://badge.fury.io/py/chunkit.svg" alt="PyPI version" /></a>
  <a href="https://pepy.tech/project/chunkit"><img src="https://pepy.tech/badge/chunkit" alt="Downloads" /></a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="License: GPL v3" /></a>
</div>

<h3 align="center">Turn URLs into LLM-friendly markdown chunks</h3>

Chunkit allows you to scrape and convert webpages into markdown chunks, for RAG applications.

### TL;DR: Quickstart

1) Install

```bash
pip install chunkit
```

2) Start chunking

```python
from chunkit import Chunker

# Initialize the Chunker
chunker = Chunker()

# Define URLs to process
urls = ["https://en.wikipedia.org/wiki/Chunking_(psychology)"]

# Process the URLs into markdown chunks
chunkified_urls = chunker.process(urls)

# Output the resulting chunks
for url in chunkified_urls:
    if url['success']:
        for chunk in url['chunks']:
            print(chunk)
```

<details>
  <summary>Example results:</summary>

Chunk 1:
```markdown
### Chunking (psychology)

In cognitive psychology, **chunking** is a process by which small individual pieces of a set of information are bound together to create a meaningful whole later on in memory. The chunks, by which the information is grouped, are meant to improve short-term retention of the material, thus bypassing the limited capacity of working memory...
```
Chunk 2:
```markdown
### Modality effect

A modality effect is present in chunking. That is, the mechanism used to convey the list of items to the individual affects how much "chunking" occurs. Experimentally, it has been found that auditory presentation results in a larger amount of grouping in the responses of individuals than visual presentation does...
```
Chunk 3:
```markdown
### Memory training systems, mnemonic

Various kinds of memory training systems and mnemonics include training and drills in specially-designed recoding or chunking schemes. Such systems existed before Miller's paper, but there was no convenient term to describe the general strategy and no substantive and reliable research...
```
Etc.

</details>


### How most chunkers work

Most chunkers work like this:

* They perform a naive chunking based on the number of words in the content.
* For example, they may split content every 200 words, and have a 30 word overlap between each.
* This leads to messy chunks that are noisy and have unnecessary extra data.
* Additionally the chunk sentences are usually split in the middle, with lost meaning.
* This leads to poor RAG/LLM performance with incorrect answers.

### Why Chunkit works better

Chunkit however, converts HTML to Markdown, and then determines split points based on the most common header levels.

This gives you better results because:

* Online content tends to be logically split in paragraphs delimited by headers.
* By chunking based on headers, this method preserves semantic meaning better.
* You get a much cleaner, semantically cohesive paragraph of data.
* You can then use Chunkit to remove noise or extract specific data.

### Supported filetypes

This free open source package primarily chunks webpages and html.

To access more filetypes, and to support the development of this package - you can use Chunkit Plus.

### Chunkit Plus

Chunkit Plus allows you to chunk more filetypes: PDF, CSV, JSON, YAML, MD and DOCX.

Chunkit Plus also offers a number of improvements:

* Captures javascript-rendered content
* Uses improved chunking algorithms
* Supports automatic noise-removal
* Performs automatic retries

To use Chunkit Plus, you need an API key:

1. Go to [app.chunkit.dev](https://app.chunkit.dev) and log in.
2. Navigate to Deploy API section.
3. Generate a new API key.
4. Initialize Chunker with API key:

```python
from chunkit import Chunker

# Initialize the Chunker with API key
chunker = Chunker(api_key='your-api-key-here')
```
That's it! The rest works as the example above.
### License

This project is licensed under GPL v3 - see the [LICENSE](LICENSE) file for details.

### Contact

For questions or support, please open an issue. 
