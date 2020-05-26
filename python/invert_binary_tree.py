# https://leetcode.com/problems/invert-binary-tree/
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def invert(root):
	if root == None:
		return
	root.left, root.right = root.right, root.left
	invert(root.left)
	invert(root.right)

def print_inorder(root):
	if root != None:
		print_inorder(root.left)
		print(root.data)
		print_inorder(root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(4)
root.right.right = Node(5)
print_inorder(root)
print('###########')	
invert(root)
print_inorder(root)
