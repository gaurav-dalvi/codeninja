# https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
# Key Learning: In tree program when you try to refer node.child.child then 
# that means your logic is incorrect . Try to think sometghing different.
# Using same tre twice and comparing it was the key here.

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def check_if_mirror(node1, node2):

	if node1 == None and node2 == None:
		return True

	if node1 != None and node2 != None:
		if node1.data == node2.data:
			return check_if_mirror(node1.left, node2.right) and check_if_mirror(node1.right, node2.left)

	return False

root = Node(1)
n1 = Node(1)
n2 = Node(1)
n3 = Node(1)
n4 = Node(1)
n5 = Node(1)
n6 = Node(1)

root.left = n1
root.right = n2
root.left.left = n3
root.right.left = n4
# root.left.left.left = n5
print check_if_mirror(root, root)
