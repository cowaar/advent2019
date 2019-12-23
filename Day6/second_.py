import networkx as nx
import matplotlib.pyplot as plt
list = open("input.txt").read().split()
print(list)
G = nx.Graph()
for item in list:
    inner,outer = item.split(")")
    print('inner = ' +inner +" outer = " + outer)
    G.add_edge(outer, inner)



for neighbour in nx.neighbors(G,"SAN"):
    santas_planet = neighbour


for neighbour in nx.neighbors(G,"YOU"):
    your_planet = neighbour

print(your_planet,santas_planet)
print(nx.shortest_path_length(G, your_planet, santas_planet))
