import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

G = nx.Graph()

G.add_node(0, pos=(1, 1))
G.add_node(1, pos=(1, 2))
G.add_node(2, pos=(2, 4))
G.add_node(4, pos=(3, 4))

G.add_edge(0, 1, weight=20, relation='friends')
G.add_edge(1, 2, weight=40, relation='enemy')
G.add_edge(2, 4, weight=60, relation='enemy')
G.add_edge(0, 4, weight=100, relation='friends')

weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
relation = nx.get_edge_attributes(G, 'relation')

dic = {'enemy': 'red', 'friends': 'blue'}

nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw_networkx(G, pos, edge_color=[dic[x] for x in relation.values()])
plt.show()

G1 = nx.DiGraph()
G1.add_edge(1, 2)
G1.add_edge(1, 3)
nx.draw_networkx(G1)
plt.show()
print(nx.info(G))
