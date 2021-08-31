import teneto
import numpy as np
import matplotlib.pyplot as plt
from teneto import TemporalNetwork

G = np.zeros([4, 4, 3])
G[0, 1, [0, 2]] = 1
G[0, 3, [2]] = 1
G[1, 2, [1]] = 1
G[2, 3, [1]] = 1

tnet: TemporalNetwork = TemporalNetwork(from_array=G, nettype='bu', diagonal=True)
tp = teneto.networkmeasures.temporal_degree_centrality(tnet, axis=0, calc='overtime', communities=None, decay=0,
                                                      ignorediagonal=True)
tc = teneto.networkmeasures.temporal_closeness_centrality(tnet, paths=None)
print(tc)
