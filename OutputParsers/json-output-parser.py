"""
    JSON OUTPUT PARSERS

    It is used to get json format output from the llm/model.
    flaws: It may use the random structure and provide data according to it.

    In it we can't spectifiy the required structure fromat according to our will.
    Inshort, we can't create our our schema.

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

parser = JsonOutputParser

template = PromptTemplate(
    template = "Give name, age and city of fictional person /n {format_instruction}",
    input_variables = [],
    partial_variables = {"format_instruction": get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({})

print(result)