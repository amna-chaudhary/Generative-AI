"""
    WEB BASE LOADER

    web scraped data ---> document abject

    1. The web base loader is used to convert web scraped data into document object.
    
"""

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    url="https://en.wikipedia.org/wiki/Generative_AI"
)

docs = loader.load()

print(docs[0].page_content)

