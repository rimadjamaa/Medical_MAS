from agents import gpt
# from src.models.pydantic_models import Answer
# from src.tools import TOOLS
#from src.tools.tools import query_aura # tu importe le tool taek
from config.prompts import (
    AGENT_INSTRUCTION,
    DIALOGUE_AGENT_PROMPT,
    COORDINATION_AGENT_PROMPT,
    SYMPTOM_CHECKER_PROMPT,
    KG_QUERY_PROMPT,
    EDUCATION_AGENT_PROMPT,
    RECOMMENDATION_AGENT_PROMPT,
    ORIENTATION_AGENT_PROMPT,
)

# Classe générique d'agent Gemini
class GeminiAgent:
    def __init__(self, prompt):
        self.prompt = prompt
        self.model = gpt

def run(self, question):
    # On combine le prompt et la question utilisateur
    full_prompt = f"{self.prompt}\n\nQuestion: {question}"
    response = self.model.generate_content(full_prompt)
    # tools=[query_aura], # tu ajoutes le tool taek pour chaque agent qui l'utilise
    return response.text

# Définition de chaque agent avec son prompt spécifique
agent = GeminiAgent(AGENT_INSTRUCTION)
agent_dialogue = GeminiAgent(DIALOGUE_AGENT_PROMPT)
agent_coordination = GeminiAgent(COORDINATION_AGENT_PROMPT)
agent_symptom_checker = GeminiAgent(SYMPTOM_CHECKER_PROMPT)
agent_kg_query = GeminiAgent(KG_QUERY_PROMPT)
agent_education = GeminiAgent(EDUCATION_AGENT_PROMPT)
agent_recommendation = GeminiAgent(RECOMMENDATION_AGENT_PROMPT)
agent_orientation = GeminiAgent(ORIENTATION_AGENT_PROMPT)