from agents.utilis import extract_response_from_agent, getAgentAnswer
from agents.agent import agent

def test_agent_dialogue():
    query = "Bonjour, pouvez-vous m'aider à prendre rendez-vous ?"
    try:
        answer = getAgentAnswer(agent, query)
        print("Réponse directe :", answer)
    except Exception as e:
        print("Erreur :", e)

if __name__ == "__main__":
    test_agent_dialogue()