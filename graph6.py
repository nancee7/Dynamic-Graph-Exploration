import teneto
import numpy as np
import matplotlib.pyplot as plt
from teneto import TemporalNetwork

nodes = 4
tsteps = 4

# G= np.zeros([nodes, nodes, tsteps])
# G[0, 1, [0, 2]] = 1
# G[0, 3, [2]] = 1
# G[1, 2, [1]] = 1
# G[2, 3, [1]] = 1

# np.random.seed(2019)
G = np.random.beta(1,1,[nodes,nodes,tsteps])
G1 = np.random.randint(2, size=(nodes,nodes, tsteps))

for start_node in range(nodes):
    for dest_node in range(start_node, nodes):
        sp = teneto.networkmeasures.shortest_temporal_path(G1, i=start_node, j=dest_node, it=0)
        print(sp)

fig, ax = plt.subplots(1)
ax = teneto.plot.slice_plot(G1, ax, timelabels=list(range(tsteps)), cmap='Set2')
plt.tight_layout()
fig.show()
plt.show()

# #i = [0, 0, 0, 1, 2, 3, 4]
# #j = [3, 4, 5, 5, 4, 5, 5]
# G[i, j] = 1
# fig, ax = plt.subplots(1)
# ax = teneto.plot.circle_plot(G, ax)
# fig.show()
# plt.show()

# sp= teneto.networkmeasures.shortest_temporal_path(G, i=0, j=3, it=0)
# sp['temporal-distance']
