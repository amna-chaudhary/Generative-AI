"""
    RUNNABLE SEQUENCE

    1. It's a primitive runnable that allows you to
    execute a sequence of runnables in order, one after the other.  
    2. It takes a list of runnables as input and executes them in 
    the order they are provided.
    

    example: joke and it's explanation

"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatOpenAI( model = "gpt-4.1-mini")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Provide a joke about the {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Provide the explanation of the {text}',
    input_variables = ['text']
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))



