from agents import AGENT_RESPONSE_KEYS
from agents.agent import agent


def extract_response_from_agent(response, agent_name):
	"""
	Extracts relevant fields from the assistant's message based on the agent's predefined keys.

	Args:
	    response: The response object returned by the agent.
	    agent_name (str): The name of the agent, used to determine expected keys.

	Returns:
	    dict: A dictionary containing the extracted key-value pairs, or None if no valid response.
	"""
	# Get expected keys for the agent, default to an empty list if not found

	expected_keys = AGENT_RESPONSE_KEYS.get(agent_name, [])
	answer = response.text
	if isinstance(answer, str):
		answer = {expected_keys[0]: answer}
		return answer
	else:
		answer = answer.dict()
		answer = {key: answer.get(key) for key in expected_keys}
		return answer
	
def getAgentAnswer(agent, query):
    """
    Envoie la question à l'agent et retourne la réponse textuelle.
    """
    result = agent.run(query)
    return result  # Ici, result est déjà une string (response.text dans GeminiAgent)