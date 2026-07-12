"""
MESSAGE PLACEHOLDER PROMPT ENIGNEERING

1. Basically this is a practice of message placeholder prompt engineering.
   In which we are using a message placeholder prompt to get the result from the model
   means using a message placeholder prompt to get the result from the model.
   The message placeholder prompt is used to store the previous messages in the conversation.
   And also we spescify the eachs message type in the conversation such as system message, human message and AI message.
   In it, model can take the extra information to provide response such as preferences etc and also

"""



from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content="You are an AI expert in Generative AI."
    ),

    MessagesPlaceholder(variable_name="chat_history"),

    HumanMessage(
        content="{question}"
    )
])

chat_history = [
    HumanMessage(content="I want the roadmap of Generative AI for one month."),
    AIMessage(content="Sure! Here is a one-month roadmap...")
]

prompt_value = prompt.invoke({
    "chat_history": chat_history,
    "question": "Can you recommend some free YouTube channels?"
})

result = model.invoke(prompt_value)

print(result.content)