from langgraph.graph import StateGraph
from typing import TypedDict, List

# Import des fonctions agents (à créer séparément dans agents/...)
from agents.agent_dialogue.main import agent_dialogue
from agents.agent_coordination.main import agent_coordination
from agents.agent_symptom_checker.main import agent_symptom_checker
from agents.agent_kg_query.main import agent_kg_query
from agents.agent_education.main import agent_education
from agents.agent_recommendation.main import agent_recommendation
from agents.agent_orientation.main import agent_orientation

# ✅ Définition du schema de données partagé entre les agents
class ChatState(TypedDict, total=False):
    input: str
    symptoms: List[str]
    next: str
    diagnosis: str
    education: str
    orientation: str
    recommendation: str
    kg_data: dict
    final_response: str

# ✅ Construction du graphe
builder = StateGraph(ChatState)

# Ajout des noeuds (agents)
builder.add_node("AgentDialogue", agent_dialogue)
builder.add_node("AgentCoordination", agent_coordination)
builder.add_node("AgentSymptomChecker", agent_symptom_checker)
builder.add_node("AgentKGQuery", agent_kg_query)
builder.add_node("AgentEducation", agent_education)
builder.add_node("AgentRecommendation", agent_recommendation)
builder.add_node("AgentOrientation", agent_orientation)

# Définition du flow entre les agents
builder.set_entry_point("AgentDialogue")

builder.add_edge("AgentDialogue", "AgentCoordination")
builder.add_edge("AgentSymptomChecker", "AgentKGQuery")
builder.add_edge("AgentEducation", "AgentRecommendation")
builder.add_edge("AgentKGQuery", "AgentOrientation")

# Tu peux rediriger tout vers une sortie finale ou centraliser dans "AgentRecommendation"
builder.add_edge("AgentOrientation", "AgentRecommendation")

builder.add_conditional_edges(
    "AgentCoordination",
    lambda state: state["next"],
    {
        "AgentSymptomChecker": "AgentSymptomChecker",
        "AgentEducation": "AgentEducation",
    }
)


# Fin du graphe sur AgentRecommendation
builder.set_finish_point("AgentRecommendation")

# Compilation du graphe
graph = builder.compile()
