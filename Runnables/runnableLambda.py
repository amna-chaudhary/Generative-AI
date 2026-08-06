"""
    RUNNABLE LAMBDA

    1. It's a primitive runnable that allows you to
    define a custom python lambda function to be executed 
    (as part of) a chain. 
    
    2. It takes a lambda function as input and executes it 
    when invoked. 
    
    example: generating a joke then
        1. printing it
        2. counting it's no of word
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda

load_dotenv()

model = ChatOpenAI('gpt-4.1-mini')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Create a joke about {topic}',
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

chain = RunnableSequence(joke_chain, parallel_chain)

result = chain.invoke({'topic': 'India'})

formated_result = """{}\nword_count": {}""".format(result['joke'], result['word_count'])
print(formated_result)