from pandas import DataFrame
import matplotlib.pyplot as plt
from teneto import TemporalNetwork
import numpy as np
import pandas as pd

tnet = TemporalNetwork()
num = np.random.seed(2019)
tnet.generatenetwork('rand_binomial', size=(5, 3), prob=0.5)
pal = tnet.get_network_when(i=1, t=0)
G = np.random.beta(1, 1, [5, 5, 3])
tnet = TemporalNetwork(from_array=G, nettype='wd', diagonal=True)
# G2 = tnet.to_array()
cat = tnet.network

tlabs = ['2014', '2015', '2016', '2017', '2018', '2020']
tunits = 'years'
nlabs = ['node1', 'node2', 'node3']
tnet = TemporalNetwork(nodelabels=nlabs, timeunit=tunits, timelabels=tlabs, nettype='bu')
tnet.generatenetwork('rand_binomial', size=(3, 6), prob=0.5)
tnet.plot('slice_plot', cmap='Set2')
plt.show()

# print(cat)
