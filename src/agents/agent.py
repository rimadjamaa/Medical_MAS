from agno.agent import Agent

from src.config.prompts import AGENT_INSTRUCTION
from src.agents import gpt
# from src.models.pydantic_models import Answer
# from src.tools import TOOLS

# ici je doit defini tt mes agents de mon medical MAS 
agent = Agent(
	name="agent",
	model=gpt,
	instructions=AGENT_INSTRUCTION,
	# response_model=Answer, # optional for structured outputs or api response
    # tools=TOOLS['agent'],  # optional for agent tools
    structured_outputs=False,
    stream=True
)