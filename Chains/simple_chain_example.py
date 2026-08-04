"""
SIMPLE CHAINS EXAMPLE

Example of using a simple chain. It makes working with prompts easier.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatOpenAI(model="gpt-4.1-mini")

# Create the prompt
prompt = PromptTemplate(
    template="Write a 5-line paragraph on {topic}.",
    input_variables=["topic"]
)

# Output parser
parser = StrOutputParser()

# Create the chain
chain = prompt | model | parser

# Invoke the chain
result = chain.invoke({"topic": "Pakistan"})

# Print the result
print(result)

# Visualizing chain
chain.get_graph().print_ascii()