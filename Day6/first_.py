import networkx as nx
import matplotlib.pyplot as plt
list = open("input.txt").read().split()
print(list)
G = nx.DiGraph()
for item in list:
    inner,outer = item.split(")")
    print('inner = ' +inner +" outer = " + outer)
    G.add_edge(outer, inner)


print(nx.shortest_path_length(G,"COM","COM"))
count = 0
for node in G.nodes:
    count = count + nx.shortest_path_length(G,node,"COM")
print(count)