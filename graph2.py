import networkx as nx
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import rcParams


rcParams ['figure.figsize'] = 5,4
sb.set_style('whitegrid')

DG = nx.gn_graph(7, seed=25)
for line in nx.generate_edgelist(DG, data=False):
    print(line)
DG.nodes[0] ['name'] = 'Alice'
DG.nodes[1] ['name'] = 'Nancy'
DG.nodes[2] ['name'] = 'Daniel'
DG.nodes[3] ['name'] = 'Agnes'
DG.nodes[4] ['name'] = 'Emma'
DG.nodes[5] ['name'] = 'Micheal'
DG.nodes[6] ['name'] = 'Segun'

DG.add_nodes_from ([(0, {'age' :25}), (1, {'age' :24}), (2, {'age' :20}), (3, {'age' :24}), (4, {'age' :29}), (5, {'age' :32}), (6, {'age' :33})])

DG.nodes[0] ['gender'] = 'f'
DG.nodes[1] ['gender'] = 'f'
DG.nodes[2] ['gender'] = 'm'
DG.nodes[3] ['gender'] = 'f'
DG.nodes[4] ['gender'] = 'm'
DG.nodes[5] ['gender'] = 'm'
DG.nodes[6] ['gender'] = 'm'

nx.draw_circular(DG, node_color ='bisque',with_labels=True)

labeldict = {0: 'Alice', 1:'Nancy', 2:'Daniel', 3:'Agnes', 4:'Emma', 5:'Micheal', 6:'Segun'}
nx.draw_circular(DG, labels= labeldict, node_color ='bisque',with_labels=True)
plt.show()
#print (DG.nodes[0])

