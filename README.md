# Terminal Search Tool

A lightweight terminal-based search and fetch tool that allows you to perform web searches and extract webpage content directly in your console. It strips away the noise (scripts, styles, navs) and presents the content in a clean, readable format.

## 🚀 Features
- **Web Search**: Quickly get search results from the web via DuckDuckGo.
- **Web Fetch**: Fetch the main text content of any URL.
- **Clean Rendering**: Uses `rich` for markdown-style rendering in the terminal.
- **Content Storage**: Option to save fetched webpages as `.md` files.

## 🛠 Installation

### Prerequisites
Ensure you have Python 3.7+ installed.

### Local Installation
Navigate to the project root directory (where `setup.py` is located) and install the package:

```bash
# Navigate to the root folder
cd /path/to/search-repo

# Install dependencies first
pip install -r requirements.txt

# Install the package
pip install .

# Or for editable installation
pip install -e .
```

## 📖 Usage

After installation, you can use the `search` and `fetch` commands from anywhere in your terminal.

### 1. Searching the Web
To search for a topic, use the `search` command followed by your query.

```bash
# Basic search
search "python programming"

# Search with a specific number of results (default is 5)
search "quantum computing" 3
```

### 2. Fetching a Webpage
To extract the content of a specific URL, use the `fetch` command.

```bash
# Fetch a page
fetch "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Fetch and save the content to a markdown file
fetch "https://example.com" --store
```

## ⚙️ Technical Notes
- **Windows Support**: The tool includes an automatic UTF-8 encoding override to ensure it works correctly on Windows terminals.
- **Dependencies**: Relies on `click`, `httpx`, `beautifulsoup4`, `rich`, and `duckduckgo-search` (mapped to `ddgs` in requirements).

## 📜 License
MIT
