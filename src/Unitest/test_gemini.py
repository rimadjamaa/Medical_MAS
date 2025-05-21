from agents import gpt
from agents.utilis import extract_response_from_agent , getAgentAnswer
from agents.agent import agent


# GPT works seccessfully
response = gpt.generate_content("Explain how AI works in a few words")

print(response.text)

# extract_response_from_agent from utilis.py works seccessfuly
response = gpt.generate_content("What is AI?")
result = extract_response_from_agent(response, "agent")  # ici la repose est retournee avec l'utilisation de l'agent
print(result)  # {'answer': 'AI is ...'}


class SimpleAgent:
    def run(self, query, structured_outputs=True, stream=False):
        # Use your Gemini model to generate a response
        response = gpt.generate_content(query)  # or use .text if your code expects it
        return response

my_agent = SimpleAgent()
answer = getAgentAnswer(my_agent, "What is AI?")
print(answer)
# Output: "AI is the simulation of human intelligence by machines." (for example)


query = "Bonjour, pouvez-vous m'aider à prendre rendez-vous ?"
response = agent.model.generate_content(query)
answer = extract_response_from_agent(response, "agent_dialogue")
print("Réponse directe :", answer)