# https://www.techiedelight.com/find-maximum-sum-root-to-leaf-path-binary-tree/
# From bottom to up approach in any tree make sure that in base case you return at root == None
# and then develop your logic in else part.

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def max_sum_root_to_leaf(root):

	if root == None:
		return 0
	else:
		m1 = root.data + max_sum_root_to_leaf(root.left) 
		m2 = root.data + max_sum_root_to_leaf(root.right) 
		return max(m1, m2)

def print_path_of_sum(root, path, target_sum):
	
	if target_sum == 0:
		return True
	if root == None:
		return False
	s1 = print_path_of_sum(root.left, path, target_sum - root.data)
	s2 = print_path_of_sum(root.right, path, target_sum - root.data)
	if s1 or s2:
		path.append(root.data)
	
	return s1 or s2

root = Node(10)
n2 = Node(-2)
n3 = Node(7)
n4 = Node(8)
n5 = Node(-4)
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5

target_sum = max_sum_root_to_leaf(root)
print(target_sum)

path = []
print_path_of_sum(root, path, target_sum)
print path
