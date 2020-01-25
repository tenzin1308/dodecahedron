import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.dodecahedral_graph()

nodes = list(nx.nodes(G))
vertex = list(nx.edges(G))
shortest_paths = dict(nx.shortest_path_length(G))

print("List of nodes ", nodes)
print("List of vertex ", vertex)
# print(np.asarray(shortest_paths))

start = int(input("Enter the starting point: "))
starting_point = shortest_paths[start]
end = int(input("Enter the ending point: "))
ending_point = starting_point[end]
# print(starting_point)
print("The length of the shortest path form", start, " to ", end , " is ",ending_point)

nx.draw_networkx(G)
info = nx.info(G)
print(info)
plt.show()

