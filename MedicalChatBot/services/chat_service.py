import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from agents.agent import agent

def get_chat_response(user_message):
    # Ici tu peux ajouter de la logique métier, logs, etc.
    return agent.run(user_message)