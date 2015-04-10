# -*- coding: utf-8 -*-
#    This code is part of the NetworkL package http://networkl.github.io
#    Copyright (C) 2015 by
#    Moreno Bonaventura <morenobonaventura@gmail.com>
#    This is Free Software - You can use and distribute it under
#    the terms of the GNU General Public License, version 3 or later.
"""
Sparse Geodesic Matrix
"""
__author__ = """Moreno Bonaventura (morenobonaventura@gmail.com)"""


import networkx as nx
import networkl as nl
from collections import defaultdict

#functions
def matrix_values_counter(Matrix):
	counter = defaultdict(int)
	for i,vals in Matrix.iteritems():
		for d in vals.values():
			counter[d]+=1
	return counter
	
def optimal_dstar(Matrix):
	counter = matrix_values_counter(Matrix)
	maxcount = max(counter.values())
	inverted = {v:k for k,v in counter.iteritems()}
	return inverted[maxcount]

def geodesic_to_sparse_geodesic(G,D):
	if not nx.is_connected(G):
		raise nl.NetworkLError('the graph is not connected')
	dstar = optimal_dstar(D)
	matrix = {i:{j:dij for j,dij in vals.iteritems() if not dij == dstar} for i,vals in D.iteritems()}
	return SparseGeoMatrix(dstar,matrix)

def sparse_distance_matrix(G):
	D = nx.all_pairs_shortest_path_length(G)
	return geodesic_to_sparse_geodesic(G,D)


#class dstar_dict
#this can be avoided by using a dict class parent
class DstarDict():
	def __init__(self,dstar=4,indict={}):
		self.dstar = dstar
		self.indict = indict
	def get(self,key,s):
		return self.indict.get(key,s)
	def __getitem__(self, key):
		return self.indict.get(key,self.dstar)
	def __setitem__(self,key,item):
		self.indict[key]=item	
		

#class sparse geodesic matrix
class SparseGeoMatrix():
	def __init__(self,dstar=4,InMatrix={}):
		self.dstar = dstar
		self.matrix = {}
		for k,v in InMatrix.iteritems():
			self.matrix[k] = DstarDict(self.dstar,v)
		self.N = len(InMatrix)

	def __getitem__(self,key):
#		if not self.matrix.has_key(key):
#			nl.NetworkLError('No row in SparseGeoMatrix')
		return self.matrix[key]
		
	def set_dstar(self,dstar):
		self.dstar = dstar

	def optimize_dstar(self):
		counter = matrix_values_counter(self.matrix)
		maxcount = max(counter.values())
		old_dstar = self.dstar
		if maxcount > self.N * self.N - sum(counter.values()):
			inverted = {v:k for k,v in counter.iteritems()}
			new_dstar = inverted[maxcount]
			for i in self.matrix.keys():
				for j in range(self.N):
					if self.get_dist(i,j) == old_dstar:
						 self.matrix[i][j] = old_dstar
					if self.get_dist(i,j) == new_dstar:
						self.matrix[i].pop(j)
			self.dstar = new_dstar	
	
	def get_dist(self,i,j):
		return self.matrix.get(i,{}).get(j,self.dstar)


