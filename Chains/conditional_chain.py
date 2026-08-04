"""
    CONDITIONAL CHAIN EXAMPLE

    Conditional chain executes one of multiple chains
    based on a condition.
"""

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser,
)

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )


feedback_parser = PydanticOutputParser(
    pydantic_object=Feedback
)


feedback_prompt = PromptTemplate(
    template="""
Classify the following feedback as positive or negative.

{format_instructions}

Feedback:
{feedback}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": feedback_parser.get_format_instructions()
    },
)


classifier_chain = (
    feedback_prompt
    | model
    | feedback_parser
)


positive_prompt = PromptTemplate(
    template="Write a thank you note for the positive feedback: {feedback}",
    input_variables=["feedback"],
)

negative_prompt = PromptTemplate(
    template="Write an apology note for the negative feedback: {feedback}",
    input_variables=["feedback"],
)


branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        positive_prompt | model | parser,
    ),
    (
        lambda x: x.sentiment == "negative",
        negative_prompt | model | parser,
    ),
    RunnableLambda(
        lambda x: "Could not determine the sentiment."
    ),
)


chain = classifier_chain | branch_chain

result = chain.invoke(
    {
        "feedback": "The product is not good."
    }
)

# print(result)

# Visualizing chain
chain.get_graph().print_ascii()