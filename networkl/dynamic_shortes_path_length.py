# -*- coding: utf-8 -*-
#    This code is part of the NetworkL package http://networkl.github.io
#    Copyright (C) 2015 by
#    Moreno Bonaventura <morenobonaventura@gmail.com>
#    This is Free Software - You can use and distribute it under
#    the terms of the GNU General Public License, version 3 or later.
"""
Dynamic Shortest Path Lengths Updating
"""
__author__ = 'Moreno Bonaventura (morenobonaventura@gmail.com)'
__all__ = ['update_distance_matrix']

import networkx as nx
import networkl as nl

#-------------- ADD update function -----------------
def add_update(G, D, i, j):
	for l in G.nodes():
		to_be_updated = set([j])
		checked = set()
		while len(to_be_updated)>0:
			for m in to_be_updated:
				tmp = D[l][i]+1+D[j][m]
				if tmp < D[l][m]:
					D[l][m] = tmp
					D[m][l] = tmp
					to_be_updated = to_be_updated.union(G.neighbors(m))
				checked.add(m)
			to_be_updated = to_be_updated.difference(checked)
	G.add_edge(i,j)
	D[i][j]=1
	D[j][i]=1
	return D	


#-------------- REMOVE update function -----------------
def find_anchor(NodesList,d,i,j):
	anchors = []
	for n in NodesList:
		#i controlli n!=i e n!=j rallentano...
		if d[n][i] == d[n][j] and (not n==i) and (not n==j):
			anchors.append(n)
	return anchors

def find_twins(EdgesList,d,i,j):
	twins = []
	for l,m in EdgesList:
		#the search for twins could be improved
		if d[i][l] == d[m][j] and d[i][m] == d[l][j] and d[l][i] < d[m][i]:
			twins.append([l,m])
		if d[i][m] == d[l][j] and d[i][l] == d[m][j] and d[m][i] < d[l][i]:
			twins.append([m,l])
	return twins

def remove_update(G, D, i, j):
	D[i][j]=D[j][i] = float('inf')
	G.remove_edge(j,i)
	NodesList = G.nodes()
	anchors = find_anchor(NodesList,D,i,j)
	EdgesList = G.edges()
	twins = find_twins(EdgesList,D,i,j)	
	for l in NodesList:
		for m in NodesList:
			DlmTmp = D[l][m]
			#if l---i-j---m is a candidate shortest path
			if D[l][i] + 1 + D[j][m] == DlmTmp or (l==i and m==j):
				flag = 1
				Dbest = float('inf')
				#check anchors
				for A in anchors:
					DlAmTmp = D[l][A] + D[A][m]
					if DlAmTmp == DlmTmp:
						Dbest = DlmTmp
						flag = 0
						break #break the search for anchors
					if DlAmTmp < Dbest:
						Dbest = DlAmTmp
				#if an alternative path is found 
				# we skip to with the next edge
				if flag == 0:
					continue
				#check twins	
				for e,f in twins:
					DlefmTmp = D[l][e]+1+D[f][m]
					if DlefmTmp == DlmTmp:
						Dbest = DlmTmp
						break
					if DlefmTmp < Dbest:
						Dbest = DlefmTmp
				
				D[l][m] = Dbest
				D[m][l] = Dbest
							
	return D,anchors,twins
	

def update_distance_matrix (G, D, i, j, mode='add'):
	"""Add or remove a new link (i,j) and update the
	   all-pairs Shortest Path Lengths matrix D.
	   
    Parameters
    ----------
    G : graph
       an undirected graph

    D : dict
    	dictionary of shortest path lengths keyed by source and target

    i,j : node
    	two nodes among which the new edge will be created/removed
    
    mode : string, (default='add')
    	variable defining which operation you want to perform
    	'add'     add an edge between i,j nodes
    	'remove'  remove the edge between i,j nodes

    Returns
    -------
    D : dict
       The updated dictionary of shortest path lengths.

	Examples
    --------
    >>> G=nx.barabasi_albert_graph(100,2)
    >>> D=nx.all_pairs_shortest_path_length(G)
    >>> i=1; j=2;
    >>> D=nx.update_distance_matrix(G,D,i,j,mode='add')

    Notes
    -----
    The initial graph G must be connected.
    The graph G is modified in place.
    """
	
	if not nx.is_connected(G):
		raise nl.NetworkLError("path_length_update() not defined for disconnected graphs.")
	if G.is_directed():
		raise nl.NetworkLError("path_length_update() not defined for directed graphs.")
	if not (i in G.nodes()):
		raise nl.NetworkLError("node %s does not exist in graph G" % i)
	if not (j in G.nodes()):
		raise nl.NetworkLError("node %s does not exist in graph G" % j)
	if i==j:
		print "Warning: node i and j are the same"
		#raise nl.NetworkLError("node i and j are the same")
		return 1
	if mode=='add' and G.has_edge(i,j):
		print "Warning: edge (%s,%s) already exists in graph G" % (i,j)
		#raise nl.NetworkLError("edge (%s,%s) already exist in graph G" % (i,j))
		return 1
	if mode=='remove' and not G.has_edge(i,j):
		print "Warning: edge (%s,%s) not exist in graph G" % (i,j)
		#raise nl.NetworkLError("edge (%s,%s) not exist in graph G" % (i,j))
		return 1

	anchors = []
	twins = []

	if mode=='add':
		D = add_update(G, D, i, j)
		
	if mode=='remove':
		D,anchors,twins = remove_update(G, D, i, j)
	
	#return D,anchors,twins



	
