""""
    RUNNABLE BRANCH

    1. It's a primitive runnable that allows you to 
    branch the execution of a chain based on a condition. 
    
    2. It takes a condition function and two branches 
    (true and false) as input. If the condition function 
    returns True, it executes the true branch; otherwise, 
    it executes the false branch.
    
    3. It's like if-else statements in programming, but for chains.
    
    example: generaing a report then applying condition
    1. if > 300 summarize
    2. Otherwise print as it is
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatOpenAI('gpt-4.1-mini')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Create a report about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following {text}',
    input_variables=['text']
)

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_chain, branch_chain)

print(chain.invoke({"topic" : "AI"}))
