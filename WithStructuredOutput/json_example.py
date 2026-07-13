"""
JSON SCHEMA EXAMPLE

enum :  similar to literal means it  like a list of possible values. 
In this case, the sentiment can only be "positive" or "negative".


| Keyword                | Purpose                                                                     | Example                                  |
| ---------------------- | --------------------------------------------------------------------------- | ---------------------------------------- |
| `title`                | Gives a name to the schema.                                                 | `"title": "Review"`                      |
| `type`                 | Specifies the data type.                                                    | `"type": "object"`                       |
| `properties`           | Defines the fields inside an object.                                        | `"properties": {...}"`                   |
| `description`          | Explains what a field should contain. Helps the LLM generate better output. | `"description": "Summary of the review"` |
| `required`             | Lists the fields that must be present.                                      | `"required": ["summary"]`                |
| `enum`                 | Restricts a value to specific options.                                      | `"enum": ["positive", "negative"]`       |
| `items`                | Defines the type of elements in an array.                                   | `"items": {"type": "string"}`            |
| `default`              | Provides a default value if none is supplied.                               | `"default": "Unknown"`                   |
| `minimum`              | Sets the minimum value for a number.                                        | `"minimum": 0`                           |
| `maximum`              | Sets the maximum value for a number.                                        | `"maximum": 100`                         |
| `minLength`            | Minimum number of characters in a string.                                   | `"minLength": 3`                         |
| `maxLength`            | Maximum number of characters in a string.                                   | `"maxLength": 100`                       |
| `minItems`             | Minimum number of elements in an array.                                     | `"minItems": 1`                          |
| `maxItems`             | Maximum number of elements in an array.                                     | `"maxItems": 5`                          |
| `format`               | Specifies a special string format.                                          | `"format": "email"`                      |
| `additionalProperties` | Allows or disallows extra fields not defined in `properties`.               | `"additionalProperties": false`          |

"""



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Simple JSON Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "Short summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative"],
            "description": "Review sentiment"
        }
    },
    "required": ["summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema,
                                                method='function_calling')

result = structured_model.invoke("""
The phone has a great camera and long battery life.
It is fast and easy to use.
Overall, I am not happy with it.
""")

print(result)