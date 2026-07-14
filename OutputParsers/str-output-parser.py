""""
    STRING OUTPUT PARSER

    Used to parse the output of the model into a string.

"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "TinyWizard/TinyWizard-7B-v0.1",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

# Prompt 1 -->  detailed Report
prompt1 = PromptTemplate(
    template = ["Write Detailed Report of: /n {topic}"],
    input_variable = ['topic']
)

# Prompt 2 -->   Summary
prompt2 = PromptTemplate(
    template = ["Write Summary of: /n {topic}"],
    input_variable = ['text']
)

parsers = StrOutputParser()

# template1 = prompt1.invoke({"topic" : "Atomic Habit"})
# result = model.invoke(template1)
# template2 = prompt2.invoke({"text" : result})
# result = model.invoke(template1)

#Using chain
chain = prompt1 | model | parsers | prompt2 | model | parsers
result = chain.invoke({"topic" : "Atomic Habit"})

print(result)
