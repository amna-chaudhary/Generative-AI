"""
    PDF LOADER
    
    pdf ---> document object
    
    1. This loader is used to convert simple pdf into a document object.

"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path=r"D:\z Mineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\Generative AI\RAG\DocumentLoaders\Files\AMNA_BIBI.pdf"
)


docs = loader.load()


print(docs[0].page_content)
