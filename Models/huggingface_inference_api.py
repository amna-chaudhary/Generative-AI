"""
    This is a simple example of using the HuggingFace LLM using api key from .env file.
    In this example, we are using the HuggingFace LLM to get a joke in 2 sentences.
"""



from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell a joke in 2 sentences.")

print(result.content)