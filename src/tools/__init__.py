from agno.knowledge.website import WebsiteKnowledgeBase
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

# Aura credentials
AURA_URI = os.getenv("NEO4J_URI") # diri uri taek, tu dois pttr ajouter ssc to avoid ssh certificate error
AURA_USER = os.getenv("NEO4J_USERNAME") # diri username taek
AURA_PASSWORD = os.getenv("NEO4J_PASSWORD") # diri password taek

driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))