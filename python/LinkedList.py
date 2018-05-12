class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList(object):

	def __init__(self):
		self.head = None

	def add_node_front(self, node):
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def add_last(self, node):
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next

			temp.next = node 

	def __len__(self):
		if self.head == None:
			return 0
		else:
			count = 0
			temp = self.head
			while temp is not None:
				count += 1
				temp = temp.next
			return count

	def __str__(self):

		if self.head == None:
			return ""
		else:
			temp = self.head
			st = ""
			while temp.next is not None:
				st = st + str(temp.value) + "->"
				temp = temp.next
			return st + str(temp.value)

	def add_after_node(self, curr_node, new_node):

		if self.head == None:
			return -1
		else:
			temp = self.head
			while temp != curr_node:
				temp = temp.next
				if temp == None:
					return -1

			if temp.next == None:
				if temp == curr_node:
					temp.next = new_node
				else:
					return -1
			else:
				old_next_node = temp.next
				temp.next = new_node
				new_node.next = old_next_node

	def delete_node(self, node):

		if self.head == None:
			return -1
		elif self.head == node:
			self.head = self.head.next
			node = None
			return 0
		
		temp = self.head
		while temp is not None and temp.next != node:
			temp = temp.next

		if temp == None:
			return -1
		else:
			temp.next = temp.next.next
			node = None
			return 0

	def reverse(self):

		if self.head == None:
			return None

		temp = self.head
		next = None
		prev = None
		while temp is not None:
			next = temp.next
			temp.next = prev
			prev = temp
			temp = next

		self.head = prev

	def reverse_r_print(self, node):
		if node == None:
			return
		else:
			self.reverse_r_print(node.next)
			print node.value

	# https://www.geeksforgeeks.org/wp-content/uploads/2009/07/Linked-List-Rverse.gif
	def recursive_r(self, node):
		if node is None or node.next is None:
			return node
		else:
			temp = self.recursive_r(node.next)
			node.next.next = node
			node.next = None
			return temp


if __name__ == '__main__':

	ll = LinkedList()
	n4 = Node(40)
	n3 = Node(30)
	n2 = Node(20)
	n1 = Node(10)
	n5 = Node(50)
	ll.add_node_front(n4)
	ll.add_node_front(n3)
	ll.add_node_front(n2)
	ll.add_node_front(n1)
	ll.add_last(n5)
	print ll
	ll.delete_node(n4)
	print ll
	# node = ll.recursive_r(ll.head)
	# l2 = LinkedList()
	# l2.head = node
	# print l2
