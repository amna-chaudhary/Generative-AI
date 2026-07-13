"""
    OPTIONAL EXAMPLE: Using structured output with optional fields.

    Used with the optional fields.
    Code can run perfectly without the optional fields, but if they are provided, 
    they will be validated and parsed correctly.

"""

from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini"
)

# schema for the structured output of the model
class Joke(TypedDict):
    joke: Annotated[str, "Tell me simple joke."]
    punchline: Annotated[Optional[str], "Tell a punchline of the joke."]

structured_model = model.with_structured_output(Joke, method="function_calling")
structured_result = structured_model.invoke("Tell a simple joke in 2 sentences.")
print(structured_result)