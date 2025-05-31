from agents import AGENT_RESPONSE_KEYS
from agents.GeminiAgent import GeminiAgent


def extract_response_from_agent(response, agent_name):
    """
    Extracts relevant fields from the assistant's message based on the agent's predefined keys.

    Args:
        response: The response object returned by the agent.
        agent_name (str): The name of the agent, used to determine expected keys.

    Returns:
        dict: A dictionary containing the extracted key-value pairs, or None if no valid response.
    """
    expected_keys = AGENT_RESPONSE_KEYS.get(agent_name, [])
    
    # Use 'content' instead of 'text'
    answer_text = getattr(response, "content", None)
    if answer_text is None:
        # fallback to 'dict()' if available
        if hasattr(response, "dict"):
            answer_dict = response.dict()
            return {key: answer_dict.get(key) for key in expected_keys}
        return None

    import json
    try:
        parsed = json.loads(answer_text)
        if isinstance(parsed, dict):
            return {key: parsed.get(key) for key in expected_keys}
    except Exception:
        if len(expected_keys) == 1:
            return {expected_keys[0]: answer_text}
    
    if len(expected_keys) == 1:
        return {expected_keys[0]: answer_text}
    
    return None
 

def getAgentAnswer(agent: GeminiAgent, query: str):
    """
    Envoie la question à l'agent et retourne la réponse structurée (dict).
    """
    return agent.run(query)