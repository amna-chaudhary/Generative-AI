"""
DYNAMIC PROMPT ENGINEERING

1. Basically this is a practice of dynamic prompt engineering.
   In which we are using a dynamic prompt to get the result from the model 
   means using a flexible prompt to get the result from the model.
   The prompt can be modified based on the input provided by the user.
   Model can take the extra information to provide response such as preferences etc 
   and also it provides the response based on the prompt.
   
"""


from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq# import streamlit as st
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

paper_input = input("Enter the paper content: ")
style_input = input("Enter the style of the summary: ")
length_input = input("Enter the length of the summary: ") 

template = PromptTemplate(
template = '''
You are a helpful assistant.
Paper: {paper_input}
Style: {style_input}
Length: {length_input}
Provide a summary of the paper in the specified style and length.
''',
input_variables=['paper_input', 'style_input', 'length_input'],
validate_template=True)

prompt = template.invoke({
    'paper_input': paper_input, 
    'style_input': style_input, 
    'length_input': length_input
    })

result = model.invoke(prompt)


print(result.content)