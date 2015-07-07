NetworkL
--------

NetworkL is a Python package which extends the scope of the NetworkX package 
to eXtra-Large time-varying graphs. It supports the manipulation and efficient 
longitudinal analysis of complex networks

Documentation
   http://networkl.github.io
Development
   https://github.com/networkl/networkl
Materials available at:
   https://github.com/morenobonaventura/networkl_material

A quick example that update the all-pairs shortest path lengths in 
an undirected graph by using the SparseGeodesicMatrix data structure:

```python
import networkx as nx
import networkl as nl
from random import randrange

N=500
G = nx.erdos_renyi_graph(N,0.1)                                #create a graph
SparseD = nl.sparse_distance_matrix(G)                         #compute the Sparse Distance Matrix

new_edges = [(randrange(N),randrange(N)) for c in range(100)]
for i,j in new_edges:                                 
    print 'adding edge (%s,%s), updating Distance Matrix...'%(i,j)
    nl.update_distance_matrix(G,SparseD,i,j,mode='add')        #add edges and update Distance Matrix

print SparseD[5][12]                                           #accessing distance values
```

Distributed under the GNU v3 license; see LICENSE.txt
    
   Copyright (C) 2015 NetworkL Developers:
   Moreno Bonaventura <m.bonaventura@qmul.ac.uk> 



