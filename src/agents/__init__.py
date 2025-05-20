import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AIzaSyBz4IlNNrcdn7yOiAc1LddtealEYsdfrRI")

# Gemini model instance 1.5
gpt = genai.GenerativeModel("gemini-1.5-flash")

AGENT_RESPONSE_KEYS = {
    "agent": ["answer"],
}

