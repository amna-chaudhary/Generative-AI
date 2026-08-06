"""
    RUNNABLE PARALLEL

    1. It's a primitive runnable that allows you to
    execute multiple chains in parallel.
    
    example: at a time create 
    1. linkedin post
    2. tweet for X
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI("gpt-4.1-mini")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Create a linkedin post about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Create a tweet for X about {topic}',
    input_variables = ["topic"]
)

parallel_chain = RunnableParallel({
    'linkedin': RunnableSequence(prompt1, model, parser),
    'tweet': RunnableSequence(prompt2, model, parser)
})

print(parallel_chain.invoke({'topic': 'AI'}))
