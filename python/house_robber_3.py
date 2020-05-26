# https://leetcode.com/problems/house-robber-iii/
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def find_best(left, right):
	max_sum = left[0] + right[0]
	if left[0] + right[1] > max_sum:
		max_sum = left[0] + right[1]
	if left[1] + right[0] > max_sum:
		max_sum = left[1] + right[0]
	if left[1] + right[1] > max_sum:
		max_sum = left[1] + right[1]	
	return max_sum

def house_robber(root):
	if root is None:
		return (0,0)
	if root.left == None and root.right==None:
		return (root.data, 0)
	left = house_robber(root.left)
	right = house_robber(root.right)
	with_node = root.data + left[1] + right[1]
	without_node = find_best(left, right)
	return (with_node, without_node)

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(8)
root.left.right = Node(10)
root.left.right.left = Node(11)
root.right.right= Node(2)

root.right.right = Node(1)
x = house_robber(root)
if x[0] < x[1]:
	print(x[1])
else:
	print(x[0])
