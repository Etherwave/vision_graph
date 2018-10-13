import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
point=[1,2,3,4]
G.add_nodes_from(point)
edglist=[(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
G.add_edges_from(edglist)
G=nx.Graph(edglist)
position = nx.circular_layout(G)
nx.draw_networkx_nodes(G,position, nodelist=point, node_color="r")
nx.draw_networkx_edges(G,position)
nx.draw_networkx_labels(G,position)
plt.show()
print(edglist)
print(point)