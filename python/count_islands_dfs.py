# https://www.geeksforgeeks.org/find-number-of-islands/
# Key Learning:
# Where to makr item = visited
# only at one place : in DFS function - Remember
# Complexity : O(rows*cols)
# creation of 2D array in python : https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# [[value for cols] for rows]
# [[value] * cols]*rows

def get_neighbours(matrix, visited, i, j):

	total_rows = len(matrix)
	total_cols = len(matrix[0])
	row = [-1,-1,0,1,-1,0,1,1]
	col = [-1,0,-1,-1,0,1,0,1]
	neighbours = []
	for k in xrange(8):
		if i+row[k] < total_rows and j+col[k] < total_cols and i+row[k] >=0 and j+col[k] >= 0:
			if matrix[i+row[k]][j+col[k]] == 1 and visited[i][j] != True:
				neighbours.append((i+row[k], j+col[k]))

	return neighbours

def DFS(matrix, visited, i, j):
	
	neighbours = get_neighbours(matrix, visited, i, j)
	visited[i][j] = True
	for each in neighbours:
		DFS(matrix, visited, each[0], each[1])

def solution(matrix):
	total_rows = len(matrix)
	total_cols = len(matrix[0])
	visited = [[False for i in xrange(total_cols)] for j in xrange(total_rows)]
	ans = 0

	for i in xrange(total_rows):
		for j in xrange(total_cols):
			if visited[i][j] != True and matrix[i][j] == 1:
				DFS(matrix, visited, i, j)
				ans += 1
	return ans


matrix = [[1, 0, 0, 0, 0],
		  [0, 0, 0, 0, 1],
		  [1, 0, 0, 1, 1],
		  [0, 0, 0, 0, 0],
		  [1, 0, 1, 0, 1]]
print solution(matrix)
