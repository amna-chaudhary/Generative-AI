"""
    SEQUENTIAL CHAIN EXAMPLE

    Example of using a sequential chain. Means making multiple steps chain.

"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

prompt1 = PromptTemplate(
    template = "Write a 5-line paragraph on {topic}.",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Write a quiz of the following text: {text}.",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic" : "Pakistan"})

print(result)

# Visualizing chain
chain.get_graph().print_ascii()