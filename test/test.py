import networkx as nx
import networkl as nl
from random import randrange

N=500
G = nx.erdos_renyi_graph(N,0.1)                                #create a graph
SparseD = nl.sparse_distance_matrix(G)                         #compute the Sparse Distance Matrix

new_edges = [(randrange(N),randrange(N)) for c in range(100)]
for i,j in new_edges:                                 
    if G.has_edge(i,j) or i==j:
        continue
    print 'adding edge (%s,%s)'%(i,j)
    nl.update_distance_matrix(G,SparseD,i,j,mode='add')    #add edges and update Distance Matrix

print SparseD[5][12]