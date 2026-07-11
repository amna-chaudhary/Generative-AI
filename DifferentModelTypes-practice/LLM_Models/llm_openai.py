from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # loading envirnonment from .env file

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

result = llm.invoke("What is a capital of Pakistan?")

print(result)


