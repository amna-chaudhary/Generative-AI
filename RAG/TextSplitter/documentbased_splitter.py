"""
    DOCUMENT-BASED SPLITTER

    1. DocumentBasedSplitter is a class that splits a document into smaller chunks based on 
    the structure of the document. 

    2. It uses the RecursiveCharacterTextSplitter from the langchain_text_splitters library 
    to perform the splitting but this time different types of (seperators) delimiters are used.

    3. Example: 
    Code is the text which we want to split into chunks. It contains classes and function so
    we use \ndef , \nclass, etc

"""

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

split = RecursiveCharacterTextSplitter

sample = """
python code:

def hello():
    print("Hello, World!")

class MyClass:
    def __init__(self):
        self.name = "MyClass"

    def greet(self):
        print(f"Hello from {self.name}!")
    
"""