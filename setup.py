"""
This is a terminal search tool. That let's you use browser in the terminal with minimal features and just reading the comtemts of the webpage in md format.
No images, no interactive features. But will add one agent feature to make it ease to search information with this tool.
"""

from setuptools import setup, find_packages

setup(
    name="search",
    version="0.0.0.1",
    packages=find_packages(),
    install_requires=[
        # Dependencies.
        # will update later from the requirements.txt
        "ddgs",
        "beautifulsoup4",   # import name is bs4, but PyPI name is beautifulsoup4
        "rich",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "search = search.main:search",
            "fetch = search.main:fetch",
        ],
    },
)