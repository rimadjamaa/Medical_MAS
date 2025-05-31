from agno.agent import Agent
from agents import gemini_model
# from src.models.pydantic_models import Answer
from tools import search_symptoms
from tools.tools import query_aura # tu importe le tool taek
from config.prompts import (
    AGENT_INSTRUCTION,
    DIALOGUE_AGENT_PROMPT,
    COORDINATION_AGENT_PROMPT,
    SYMPTOM_CHECKER_PROMPT,
    KG_QUERY_PROMPT,
    EDUCATION_AGENT_PROMPT,
    RECOMMENDATION_AGENT_PROMPT,
)

# Définition de chaque agent avec son nom, modèle et prompt
agent = Agent(
    name="symptom_checker",
    model=gemini_model,
    instructions="You are a medical assistant who checks symptoms.",
)

agent_dialogue = Agent(
    name="agent_dialogue",
    model=gemini_model,
    instructions=DIALOGUE_AGENT_PROMPT,
    tools=[search_symptoms],
)

agent_symptom_checker = Agent(
    name="agent_symptom_checker",
    model=gemini_model,
    instructions=SYMPTOM_CHECKER_PROMPT
)

agent_coordination = Agent(
    name="agent_coordination",
    model=gemini_model,
    instructions=COORDINATION_AGENT_PROMPT
)

agent_kg_query = Agent(
    name="agent_kg_query",
    model=gemini_model,
    instructions="""
        You are a knowledge graph query agent. 
        Your task is to generate an appropriate Cypher query from the user question, 
        and use the tool 'query_aura' to execute it.
        Return only the relevant information from the result.
        also i want to see your cypher query in the response 
    """,
    tools=[query_aura]
)

agent_education = Agent(
    name="agent_education",
    model=gemini_model,
    instructions=EDUCATION_AGENT_PROMPT
)

agent_recommendation = Agent(
    name="agent_recommendation",
    model=gemini_model,
    instructions=RECOMMENDATION_AGENT_PROMPT
)




agents_dic = {
    "AgentDialogue": agent_dialogue,
    "AgentCoordination": agent_coordination,
    "AgentSymptomChecker": agent_symptom_checker,
    "AgentKGQuery": agent_kg_query,
    "AgentEducation": agent_education,
    "AgentRecommendation": agent_recommendation,
}
