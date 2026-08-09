"""
TEXT LOADER

txt ---> Document object

1. The TextLoader is used to convert text files
   into Document objects.
"""

from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    file_path=r"D:\z Mineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\Generative AI\RAG\DocumentLoaders\Files\sample.txt"
)

docs = loader.load()

print('\n')
print("Loaded successfully!")
print(docs[0].page_content)