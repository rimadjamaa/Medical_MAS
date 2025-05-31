from langgraph.graph import StateGraph
from typing import TypedDict, List, Callable

# ✅ Ton schéma d'état partagé entre agents
class ChatState(TypedDict, total=False):
    input: str
    symptoms: List[str]
    next: str
    diagnosis: str
    education: str
    orientation: str
    recommendation: str
    kg_data: dict
    final_response: str

# ✅ Fonction générique pour construire un graphe
def build_graph(
    agents: dict[str, Callable],
    entry_point: str,
    finish_point: str,
    edges: list[tuple[str, str]],
    conditional_edges: list[tuple[str, Callable, dict[str, str]]] = []
):
    builder = StateGraph(ChatState)

    # Ajouter les noeuds
    for name, agent in agents.items():
        builder.add_node(name, agent)

    # Définir le point d'entrée
    builder.set_entry_point(entry_point)

    # Ajouter les transitions directes
    for from_node, to_node in edges:
        builder.add_edge(from_node, to_node)

    # Ajouter les transitions conditionnelles
    for node_name, condition_fn, branches in conditional_edges:
        builder.add_conditional_edges(node_name, condition_fn, branches)

    # Définir le point final
    builder.set_finish_point(finish_point)

    return builder.compile()
