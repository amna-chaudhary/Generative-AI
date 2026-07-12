""""
    ANNOTATED TYPED DICT

    In it we provide more guidance about what we want to get from the model.
    Its same like typed dict but in it we also provide the description about the each key in the typed dict.
    
"""
from typing import TypedDict, Annotated

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Joke(TypedDict):
    joke: Annotated[str, "A simple joke in 2 sentences."]
    punchline: Annotated[str, "The punchline of the joke."]

model = ChatOpenAI(model="gpt-4.1-mini")

structured_model = model.with_structured_output(
    Joke,
    method="function_calling",
    include_raw=True
)

result = structured_model.invoke("Tell me a joke.")

print(result)