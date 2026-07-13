"""
PYDANTIC

Pydantic is a Python library used for data validation and parsing based on
Python type annotations. It ensures that the data you work with is
structured, validated, and of the correct type.

That's why it is widely used with FastAPI.



Literal :  we add when we want to restrict the value of a field to a specific 
set of values. i.e Negative/Positive and Male/Female etc

BaseModel : we add when we want to create a model with fields and their types.

Annotated : we add when we want to add the description of the field in the model.

Field : also when we add when we want to add the description of the field in the model.
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI()

class Joke(BaseModel):
    joke: str = Field(description="A simple joke in 2 sentences.")
    punchline: str = Field(description="The punchline of the joke.")


structured_model = model.with_structured_output(Joke)

result = structured_model.invoke("""
        Why don't skeletons fight each other? 
        They don't have the guts."""
)



print(result)
