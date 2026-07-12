"""
PYDANTIC

Pydantic is a Python library used for data validation and parsing based on
Python type annotations. It ensures that the data you work with is
structured, validated, and of the correct type.

That's why it is widely used with FastAPI.
"""

from pydantic import BaseModel


class Joke(BaseModel):
    joke: str


new_joke = {
    "joke": "Why don't skeletons fight each other? They don't have the guts."
}

joke = Joke(**new_joke)

print(joke)
print(joke.joke)