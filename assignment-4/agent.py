from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from browser_tools import (
    navigate_to,
    click_element,
    type_text,
)

from memory import memory

llm = ChatOpenAI(
    temperature=0
)

tools = [
    navigate_to,
    click_element,
    type_text
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    memory=memory,
    verbose=True
)