from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
from .symptom_tools import search_symptoms
from .recommendation_tools import recommend_specialist

load_dotenv()

# Aura credentials
AURA_URI = os.getenv("NEO4J_URI") # diri uri taek, tu dois pttr ajouter ssc to avoid ssh certificate error
AURA_USER = os.getenv("NEO4J_USERNAME") # diri username taek
AURA_PASSWORD = os.getenv("NEO4J_PASSWORD") # diri password taek

driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))

try:
    with driver.session() as session:
        session.run("RETURN 1")
        print("✅ Successfully connected to Neo4j Aura!")
except Exception as e:
    print(f"❌ Failed to connect to Neo4j Aura: {e}")
finally:
    driver.close()

TOOLS = {
    "search_symptoms": search_symptoms,
    "recommend_specialist": recommend_specialist,
}
