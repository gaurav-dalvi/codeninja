# https://www.youtube.com/watch?v=jwzo6IsMAFQ
# key learnings :
# 1: Always pass list or some collection because it gets pass by value and never pass single int (look at index)
# 2: just remeber preorder traversal.
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

# its nothing but preorder traversal
def serialize_binary_tree(node, arr):

	if node:
		arr.append(str(node.data))
		serialize_binary_tree(node.left, arr)
		serialize_binary_tree(node.right, arr)
	else:
		arr.append('#')

# remember we increase index in first if case and then increase only once and not before 
# root.right call
def deserialize_binary_tree(arr, index):
	if index[0] == len(arr) or arr[index[0]] == '#':
		index[0] += 1
		return None
	root = Node(int(arr[index[0]]))
	index[0] += 1
	root.left = deserialize_binary_tree(arr, index)
	root.right = deserialize_binary_tree(arr, index)
	return root

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.right.right = Node(25)
arr = []
serialize_binary_tree(root, arr)
print arr

index = [0]
x = deserialize_binary_tree(arr, index)
arr = []
serialize_binary_tree(x, arr)
print arr
