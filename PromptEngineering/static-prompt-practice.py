"""
STATIC PROMPT ENGINEERING

1. Basically this is a practice of static prompt engineering.
   In which we are using a static prompt to get the result from the model 
   means using a fixed prompt to get the result from the model.
   The prompt is fixed and the model will always give the same output for the same prompt.
   In it, model can't take the extra information to provide response such as preferences etc 
   and also it provides the response based on the prompt.

"""



from langchain_groq import ChatGroq
from dotenv import load_dotenv
# import streamlit as st

load_dotenv()
model = ChatGroq(
    model="llama-3.1-8b-instant"
)

# st.header("Topic Summarizer")

user_input = input("Enter your Prompt: ")
result = model.invoke(user_input)
print(result.content)



# .\venv\Scripts\Activate           to activate the virtual environment   