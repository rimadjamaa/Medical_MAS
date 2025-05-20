from graph import graph

# Entrée utilisateur simulée
user_input = input("🧑 Entrez vos symptômes : ")

# Exécution du graphe avec l'état initial
result = graph.invoke({"input": user_input})

# Affichage du résultat final
print("\n💬 Réponse finale générée par le système :")
print(result.get("final_response", "Aucune réponse."))
