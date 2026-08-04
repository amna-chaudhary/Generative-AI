"""
    PARALLEL CHAIN EXAMPLE

    Running multiple chains at the same time.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write 2 line of national anthem of {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write 3 interesting facts about {topic} in proper points.",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="Merge both of the following description: {description} /n facts: {facts}.",
    input_variables=["description", "facts"]
)


parallel_chain = RunnableParallel({
    'description' : prompt1 | model | parser,
    "facts" : prompt2 | model | parser
})


merge_chain = prompt3 | model | parser
chain = parallel_chain | merge_chain

result = chain.invoke(
    {"topic": "Pakistan"}
)

print(result)# Visualizing chain
chain.get_graph().print_ascii()