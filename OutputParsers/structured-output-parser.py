"""
    STRUCTURES OUTPUT PARSER

    similar to JSON OUTPUT PARSER used to extract json output from the model/llm 
    but in a structured format. 

    In it we can spectifiy the required structure fromat according to our will.
    Inshort, we can create our our schema.

"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "TinyWizard/TinyWizard-7B-v0.1",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

#Schema
Schema = [
    ResponseSchema = (name = "fact-1", description = "Tell the fact 1 of the topic."),
    ResponseSchema = (name = "fact-2", description = "Tell the fact 2 of the topic."),
    ResponseSchema = (name = "fact-3", description = "Tell the fact 3 of the topic.")
]

parsers = StructuredOutputParser.from_response_schema(Schema)

template = PromptTemplate(
    template = "Give me three facts abput topic: [topic] \n {format_instruction}",
    input_variable = ["topic"],
    partial_variables = ["format_instruction" : parser.get_format_instruction()]
)

chain = template | model | parsers

result = chain.invoke({"topic": "Pakistan"})

print(result)