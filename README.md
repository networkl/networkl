NetworkL
--------

NetworkL is a Python package which extends the scope of the NetworkX package 
to eXtra-Large time-varying graphs. It supports the manipulation and efficient 
longitudinal analysis of complex networks

Documentation
   http://networkl.github.io
Development
   https://github.com/networkl/networkl
   

A quick example that update the all-pairs shortest path lengths in 
an undirected graph by using the SparseGeodesicMatrix data structure:

   >>> import networkx as nx
   >>> import networkl as nl
   >>> from random import randrange
   >>>   
   >>> N=1000
   >>> G = nx.erdos_renyi_graph(N,0.1)                                 #create a graph
   >>> SparseD = nl.sparse_distance_matrix(G)                          #compute the Sparse Distance Matrix
   >>>
   >>> new_edges = [(randrange(N),randrange(N)) for c in range(100)]   #add edges and update Distance Matrix
   >>> for i,j in new_edges:
   >>>     if G.has_edge(i,j) or i==j:
   >>>		continue                   
   >>>     nl.update_distance_matrix(G,SparseD,i,j,mode='add')         
   >>>   
   >>> print SparseD[1][1]                                             #accessing distance values


Distributed under the GNU v2 license; see LICENSE.txt::
    
   Copyright (C) 2015 NetworkL Developers
   Moreno Bonaventura <m.bonaventura@qmul.ac.uk> 



