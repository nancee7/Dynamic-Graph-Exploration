import teneto
import numpy as np
import matplotlib.pyplot as plt
from teneto import TemporalNetwork
import time

import sys, getopt

def main(argv):
   nodes = ''
   tsteps = ''
   visited = []

   try:
      opts, args = getopt.getopt(argv,"hn:t:",["nodes=","tsteps="])
   except getopt.GetoptError:
      print('test.py -n <nodes> -t <tsteps>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -n <nodes> -t <tsteps>')
         sys.exit()
      elif opt in ("-n", "--nodes"):
         nodes = int(arg)
      elif opt in ("-t", "--tsteps"):
         tsteps = int(arg)
   print ('No. of nodes is ', nodes)
   print ('No. of time-steps is ', tsteps)

   #G = np.random.beta(1, 1, [nodes, nodes, tsteps])
   G1 = np.random.randint(2, size=(nodes, nodes, tsteps))
   # print('The graph is ', G1)

   start_one = time.time()
   for start_node in range(nodes):
       for dest_node in range(start_node, nodes):
          sp = teneto.networkmeasures.shortest_temporal_path(G1, i=start_node, j=dest_node, it=0)
          print(sp)
   end_one = time.time()

   start_two = time.time()
   for start_node in range(nodes):
      if start_node not in visited:
         for dest_node in range(start_node, nodes):
            sp = teneto.networkmeasures.shortest_temporal_path(G1, i=start_node, j=dest_node, it=0)
            print(sp)
            visited.append(dest_node)
      if start_node not in visited:
          visited.append(start_node)
   end_two = time.time()

   print("Time taken by first approach: {}".format(end_one - start_one))
   print("Time taken by second approach: {}".format(end_two - start_two))
   print("Visited - {}".format(visited))

   tnet: TemporalNetwork = TemporalNetwork(from_array=G1, nettype='bu', diagonal=True)
   tp = teneto.networkmeasures.temporal_degree_centrality(tnet, axis=0, calc='overtime', communities=None, decay=0,
                                                          ignorediagonal=True)
   tc = teneto.networkmeasures.temporal_closeness_centrality(tnet, paths=None)
   print('The temporal degree centrality is ', tc)
   print('The temporal closeness centrality is ', tp)

   fig, ax = plt.subplots(1)
   # ax = teneto.plot.slice_plot(G1, ax, timelabels=list(range(tsteps)), cmap='Set2')
   for tstep in range(tsteps):
      ax = teneto.plot.circle_plot(G1[:,:,tstep], ax, nodesize=nodes, cmap='Set2')
      plt.tight_layout()
      fig.show()
      plt.show()




if __name__ == "__main__":
   main(sys.argv[1:])
