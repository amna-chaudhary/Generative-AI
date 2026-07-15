"""
    PYDANTIC OUTPUT PARSER

    used to enforce schema validation when processing LLm/model's response.
    1. strict schema enforcement (well-defined structure)
    2. Type Safety (Auto convert into python's object)
    3. Easy Validation (Use pydantic buildin validation)
    4. Seamless Interogation (Work well with other langchain components)
    
"""


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)