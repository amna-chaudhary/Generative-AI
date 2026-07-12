"""
    This is a simple example of using the OpenAI LLM using api key from .env file.
    In this example, we are using the OpenAI Chat Model to get a joke in 2 sentences.
"""



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-3.5-turbo")

result = llm.invoke("Give 5 business idea in 2 words for each.", temperature = 0.5, max_tokens = 10)
result1 = llm.invoke("Give 5 business idea in 2 words for each.", temperature = 1.8, max_tokens = 10)


print(result.content)
print(result1.content)