import sys
import os
import json
from flask import jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from graph.utilis import graph
from agents.agent import agent, agent_dialogue, agent_coordination, agent_symptom_checker, agent_education, agent_kg_query
from agents.utilis import extract_response_from_agent

# def debug_agents(user_message):
#     print("Testing AgentDialogue...")
#     out1 = agent_dialogue.run(user_message)
#     print("AgentDialogue output:", out1, type(out1))

#     print("Testing AgentCoordination...")
#     out2 = agent_coordination.run(out1)
#     print("AgentCoordination output:", out2, type(out2))

#     print("Testing AgentSymptomChecker...")
#     out3 = agent_symptom_checker.run(out1)
#     print("AgentSymptomChecker output:", out3, type(out3))

#     print("Testing AgentEducation...")
#     out4 = agent_education.run(out1)
#     print("AgentEducation output:", out4, type(out4))

def test_graph(user_message):
    result = graph.run({"input": user_message})
    print("Graph output:", result)
    
    return(result)


def test_agent_response(user_message):
    result = agent_kg_query.run(user_message)
    extracted = extract_response_from_agent(result, "agent_dialogue")
    coord_response = agent_coordination.run(str(extracted))
    print(result.content)

# def get_chat_response(user_message):
#     try:
#         response = agent_dialogue.run(user_message)
#         coordination_result = agent_coordination.run(response)

#         # Parse JSON if needed
#         if isinstance(coordination_result, str):
#             coordination_result = json.loads(coordination_result)

#         next_agents = coordination_result.get("next_agents", [])
#         results = {}

#         if "agent_education" in next_agents:
#             try:
#                 results["education"] = agent_education.run(response)
#             except Exception as e:
#                 results["education"] = f"Error: {str(e)}"

#         if "agent_symptom_checker" in next_agents:
#             try:
#                 results["symptom_checker"] = agent_symptom_checker.run(response)
#             except Exception as e:
#                 results["symptom_checker"] = f"Error: {str(e)}"

#         results["coordination"] = coordination_result
#         return results

#     except Exception as e:
#         # Log the error and return a user-friendly message
#         print(f"❌ ERROR in get_chat_response: {e}")
#         return {"error": "Sorry, something went wrong.", "details": str(e)}