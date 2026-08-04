"""
    CONDITIONAL CHAIN EXAMPLE:

    Conditonal chain used when we have two conditions and at a time one will execute according to the suituation.
"""

from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import ConditionalChain
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()