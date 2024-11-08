from langchain.agents import AgentExecutor
from langchain.agents.openai import OpenAIFunctionsAgent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

class BaseAgent:
    def __init__(self, llm=None, memory=None):
        self.llm = llm or ChatOpenAI(temperature=0)
        self.memory = memory or ConversationBufferMemory()