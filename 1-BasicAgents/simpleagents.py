from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#Create agent
agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are an assistant who replied to the questions asked",
    tools=[DuckDuckGoTools()],
    markdown=True #displays the output in markdown format
)

agent.print_response("Who won the Champions Trophy 2025")

