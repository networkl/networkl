# -*- coding: utf-8 -*-
#    This code is part of the NetworkL package http://networkl.github.io
#    Copyright (C) 2015 by
#    Moreno Bonaventura <morenobonaventura@gmail.com>
#    This is Free Software - You can use and distribute it under
#    the terms of the GNU General Public License, version 3 or later.
"""
NetworkL
========

    NetworkL is a Python package which extends the scope of the NetworkX 
    package to eXtra-Large time-varying graphs. It supports the manipulation 
    and efficient longitudinal analysis of complex networks

    https://networkl.github.io/

Using
-----
    Just write in Python:
    
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
"""
__author__   = 'Moreno Bonaventura <morenobonaventura@gmail.com>'

import sys

if sys.version_info[:2] < (2, 6):
    m = "Python version 2.6 or later is required for NetworkL (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys



#These are import orderwise
from networkl.exception import  *

import networkl.dynamic_shortes_path_length
from networkl.dynamic_shortes_path_length import *

import networkl.sparse_geodesic_matrix
from networkl.sparse_geodesic_matrix import *
