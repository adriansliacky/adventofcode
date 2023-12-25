import math
import networkx as nx


with open("input.txt") as file:
    LINES = file.read().strip().splitlines()

graph = nx.Graph()


total = 0
for line in LINES:
    node, edges = line.split(": ")
    edges = edges.split()
    graph.add_node(node)
    for edge in edges:
        graph.add_edge(node, edge)

node_cut = nx.minimum_edge_cut(graph)
for a, b in node_cut:
    graph.remove_edge(a, b)

print(math.prod(len(x) for x in list(nx.connected_components(graph))))
