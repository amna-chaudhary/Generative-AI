"""
    RUNNABLE PASSTHROUGH

    1. It's a primitive runnable that allows you to
    pass the input to the next runnable in the chain without any modification.
    
    2. input is actually the output as it is.

    example: generating a joke then
    1. printing it (RunnablePassthrough)
    2. it explanation
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

model = ChatOpenAI('gpt-4.1-mini')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Create a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Provide explanation of the following {text}',
    input_variables=['text']
)

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

print(final_chain.invoke({'topic': 'India'}))