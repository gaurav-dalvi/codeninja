# Detect a cycle in undirected graph.
# https://www.geeksforgeeks.org/union-find/
# Initialize for all vertices - parent[v] = -1
# Algorighm:
# 	For each edge E(a,b)
# 		if both parents are equal then there is cycle
# 		else:
# 			do union (adjust parent values for vertices)
# Time complexity :	O(N)
# With union ny rank and find by height can be done in O(Log N)

from collections import defaultdict

class DisjointSet:

	def __init__(self, parent, rank):
		self.parent = parent
		self.rank = rank

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.edges = defaultdict(list)

	def add_edge(self, a ,b):
		self.edges[a].append(b)

def find(subsets, node):
	
	if subsets[node].parent != node:
		subsets[node].parent = find(subsets, subsets[node].parent)
	return subsets[node].parent

def union(subsets, u, v):

	if subsets[u].rank > subsets[v].rank:
		subsets[v].parent = u
	elif subsets[u].rank < subsets[v].rank:
		subsets[u].parent = v
	else:
		subsets[u].parent = v
		subsets[v].rank += 1

def is_cycle(graph):

	subsets = []
	for u in range(graph.V):
		subsets.append(DisjointSet(u, 0))

	for u in graph.edges:
		u_rep = find(subsets, u)

		for v in graph.edges[u]:
			v_rep = find(subsets, v)
			if u_rep == v_rep:
				return True
			else:
				union(subsets, u_rep, v_rep)

	return False

g = Graph(3) 
g.add_edge(0, 1) 
g.add_edge(1, 2) 
g.add_edge(0, 2) 
  
if is_cycle(g): 
    print('Graph contains cycle') 
else: 
    print('Graph does not contain cycle')
