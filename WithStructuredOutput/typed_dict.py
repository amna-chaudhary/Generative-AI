"""
    Simply used to define the TypedDict (Dictionary) for the structured output of the model.
    means before creating the dictionary we have to define the structure (uisng class) of the dictionary.

"""

from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# schema for the structured output of the model
class Joke(TypedDict):
    joke: str
    punchline:str

structured_model = model.with_structured_output(Joke)
structured_result = structured_model.invoke("Tell a simple joke in 2 sentences.")
print(structured_result)