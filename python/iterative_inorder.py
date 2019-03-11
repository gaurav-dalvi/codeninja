class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def add_nodes_left(node, stack):
	while node is not None:
		stack.append(node)
		node = node.left

def iterative_inorder(temp_node):
	stack = []
	add_nodes_left(temp_node, stack)
	
	while len(stack) != 0:
		item = stack.pop()
		print(item.data)
		if item.right:
			add_nodes_left(item.right, stack)

def r_inorder(temp_node):

	if temp_node:
		r_inorder(temp_node.left)
		print(temp_node.data)
		r_inorder(temp_node.right)

root = Node(10)
root.left = Node(6)
root.left.left = Node(4)
root.left.right = Node(8)
root.right = Node(16)
root.right.right = Node(18)
root.right.left = Node(14)
iterative_inorder(root)
