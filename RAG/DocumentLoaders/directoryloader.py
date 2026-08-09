"""
    DIRECTORY LOADER    

    Folder ---> document object

    1. The directory loader is used to convert multiple (types of .txt, .pdf etc) files in a folder into document objects.

"""

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    path=r"D:\z Mineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\Generative AI\RAG\DocumentLoaders\Files",
    glob="**/*"
)

docs = loader.load()

print('\n')
print("Loaded successfully!")   
print(docs)