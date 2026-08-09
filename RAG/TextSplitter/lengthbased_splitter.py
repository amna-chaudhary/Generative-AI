from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=0,
)

text = """
My name is Amna Afzal. I am 22 year old. 
I live in Kotla arab ali khan. 
I love Pakistan but don't want to stay here.
"""

print("\nChunks:")
chunks = text_splitter.split_text(text)

print(chunks)