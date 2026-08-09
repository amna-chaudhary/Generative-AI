"""
    CSV LOADER
    
    csv ---> document object
    
    1. The csv loader is used to convert csv files into document objects.

"""

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path=r"D:\z Mineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\Generative AI\RAG\DocumentLoaders\Files\currency.csv",
    encoding="utf-8"
)

docs = loader.load()

print(docs[0].page_content)