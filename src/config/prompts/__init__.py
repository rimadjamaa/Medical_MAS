import os

from .utils import load_prompt

# Define paths to the `.md` files
PROMPTS_DIR = os.path.dirname(__file__)
AGENT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "agent.md")
AGENT_DIALOGUE_PATH = os.path.join(PROMPTS_DIR, "agent_dialogue.md")
AGENT_COORDINATION_PATH = os.path.join(PROMPTS_DIR, "agent_coordination.md")
AGENT_SYMPTOM_CHECKER_PATH = os.path.join(PROMPTS_DIR, "agent_symptom_checker.md")
AGENT_KG_QUERY_PATH = os.path.join(PROMPTS_DIR, "agent_kg_query.md")
AGENT_EDUCATION_PATH = os.path.join(PROMPTS_DIR, "agent_education.md")
AGENT_RECOMMENDATION_PATH = os.path.join(PROMPTS_DIR, "agent_recommendation.md")
AGENT_ORIENTATION_PATH = os.path.join(PROMPTS_DIR, "agent_orientation.md")

# Load prompts
AGENT_INSTRUCTION = load_prompt(AGENT_INSTRUCTION_PATH)
DIALOGUE_AGENT_PROMPT = load_prompt(AGENT_DIALOGUE_PATH)
COORDINATION_AGENT_PROMPT = load_prompt(AGENT_COORDINATION_PATH)
SYMPTOM_CHECKER_PROMPT = load_prompt(AGENT_SYMPTOM_CHECKER_PATH)
KG_QUERY_PROMPT = load_prompt(AGENT_KG_QUERY_PATH)
EDUCATION_AGENT_PROMPT = load_prompt(AGENT_EDUCATION_PATH)
RECOMMENDATION_AGENT_PROMPT = load_prompt(AGENT_RECOMMENDATION_PATH)
ORIENTATION_AGENT_PROMPT = load_prompt(AGENT_ORIENTATION_PATH)