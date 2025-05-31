from agents.agent import agents_dic  # this is the dictionary with all your Agent() instances
from .utilis import build_graph

graph = build_graph(
    agents=agents_dic,
    entry_point="AgentDialogue",
    finish_point="AgentRecommendation",
    edges=[
        ("AgentDialogue", "AgentCoordination"),
        ("AgentSymptomChecker", "AgentKGQuery"),
        ("AgentEducation", "AgentRecommendation"),
        ("AgentKGQuery", "AgentRecommendation"),
    ],
    conditional_edges=[
        (
            "AgentCoordination",
            lambda state: state["next"],
            {
                "AgentSymptomChecker": "AgentSymptomChecker",
                "AgentEducation": "AgentEducation",
            },
        )
    ]
)
