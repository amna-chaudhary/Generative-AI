# """
#   This is a simple example of using the OpenAI LLM using api key from .env file.
#   In this example, we are using the OpenAI LLM to get the capital of Pakistan.
#   model to get the capital of Pakistan.

# """


from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # loading envirnonment from .env file

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

result = llm.invoke("What is a capital of Pakistan?")

print(result)


