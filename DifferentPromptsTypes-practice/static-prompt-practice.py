from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGroq(
    model="llama-3.1-8b-instant"
)

st.header("HELLO WORLD")

user_input = st.text_input("Enter your Prompt: ")
result = model.invoke(user_input)
st.write("Hello World")



# .\venv\Scripts\Activate           to activate the virtual environment   