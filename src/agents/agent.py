from agno.agent import Agent

from src.config.prompts import (
    AGENT_INSTRUCTION,
    DIALOGUE_AGENT_PROMPT,
    COORDINATION_AGENT_PROMPT,
    SYMPTOM_CHECKER_PROMPT,
    KG_QUERY_PROMPT,
    EDUCATION_AGENT_PROMPT,
    RECOMMENDATION_AGENT_PROMPT,
    ORIENTATION_AGENT_PROMPT,
)
from src.agents import gpt
# from src.models.pydantic_models import Answer
# from src.tools import TOOLS
from src.tools.tools import query_aura # tu importe le tool taek

# ici je doit defini tt mes agents de mon medical MAS 
agent = Agent(
	name="agent",
	model=gpt,
	instructions=AGENT_INSTRUCTION,
    # tools=[query_aura], # tu ajoutes le tool taek pour chaque agent qui l'utilise
	# response_model=Answer, # optional for structured outputs or api response
    # tools=TOOLS['agent'],  # optional for agent tools
    structured_outputs=False,
    stream=True
)


# Agent: Dialogue
agent_dialogue = Agent(
    name="agent_dialogue",
    model=gpt,
    instructions=DIALOGUE_AGENT_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: Coordination
agent_coordination = Agent(
    name="agent_coordination",
    model=gpt,
    instructions=COORDINATION_AGENT_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: Symptom Checker
agent_symptom_checker = Agent(
    name="agent_symptom_checker",
    model=gpt,
    instructions=SYMPTOM_CHECKER_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: KG Query
agent_kg_query = Agent(
    name="agent_kg_query",
    model=gpt,
    instructions=KG_QUERY_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: Education
agent_education = Agent(
    name="agent_education",
    model=gpt,
    instructions=EDUCATION_AGENT_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: Recommendation
agent_recommendation = Agent(
    name="agent_recommendation",
    model=gpt,
    instructions=RECOMMENDATION_AGENT_PROMPT,
    structured_outputs=False,
    stream=True
)

# Agent: Orientation
agent_orientation = Agent(
    name="agent_orientation",
    model=gpt,
    instructions=ORIENTATION_AGENT_PROMPT,
    structured_outputs=False,
    stream=True
)