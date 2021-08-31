import dynetx as dn
import matplotlib.pyplot as plt

g = dn.DynGraph(edge_removal=True)

g.add_interaction(u=1, v=2, t=0)
g.add_interaction(u=1, v=2, t=0, e=3)

g.add_interactions_from([(1, 2), (2, 3), (3, 1)], t=2)

s = g.time_slice(t_from=2, t_to=3)
for e in g.stream_interactions():
    print(e)
plt.show()
