import google.generativeai as genai
from agno.models.google import Gemini

# Gemini API key
gemini_model = Gemini("gemini-1.5-flash", api_key="AIzaSyBz4IlNNrcdn7yOiAc1LddtealEYsdfrRI")



AGENT_RESPONSE_KEYS = {
    "agent_dialogue": ["symptoms", "maladies", "uncertainties", "suggested_next_step"],
    "agent_coordination": ["some_key1", "some_key2"],
}

