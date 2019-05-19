# https://www.geeksforgeeks.org/disjoint-set-data-structures/
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# This data structure keeps a track of set of elements partitioned into 
# number of disjoint sets (non overlapping)
# Applications:
# 1: To detect cycle in graph:
# 2: To find direct of indirect friends : https://www.geeksforgeeks.org/disjoint-set-data-structures/

class DisjointSet:

	def __init__(self, n):
		self.n = n
		self.parent = [0] * n
		self.rank = [0] * n
		for i in xrange(n):
			self.parent[i] = i

	def find(self, x): #O(N)
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])

		return self.parent[x]

	# def find(self, x): # O(Log N)
	# 	if self.parent[x] == x:
	# 		return x
	# 	else:
	# 		result = self.find(self.parent[x])
	# 		self.parent[x] = result
	# 		return result

	# def union(self, x, y): O(Log N) This is optimization
	# 	x_parent = self.find(x)
	# 	y_parent = self.find(y)
	# 	if x_parent == y_parent:
	# 		return
	# 	if self.rank[x_parent] < self.rank[y_parent]:
	# 		self.parent[x_parent] = y_parent
	# 	elif self.rank[x_parent] > self.rank[y_parent]:
	# 		self.parent[y_parent] = x_parent
	# 	else:
	# 		self.parent[y_parent] = x_parent
	# 		self.rank[x_parent] += 1

	def union(self, x, y): #O(N)
		x_parent = self.find(x)
		y_parent = self.find(y)
		self.parent[x_parent] = y_parent

d = DisjointSet(5)
# print d.parent, d.rank
d.union(0,2)
print d.parent, d.rank
d.union(4,2)
print d.parent, d.rank
d.union(3,1)
print d.parent, d.rank
# To check if 4 is friend of 0 or not :
if d.find(4) == d.find(0):
	print '0 and 4 are friends'
else:
	print '0 and 4 are NOT friends'

# To check if 1 is friend of 0 or not :
if d.find(1) == d.find(0):
	print '0 and 1 are friends'
else:
	print '0 and 1 are NOT friends'
