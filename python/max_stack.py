# https://www.youtube.com/watch?v=0bpDvc2VjPU
# Key learning: 
# 1: get_min or get_max can be done using this special linked list node approach 
# rather than using entirely different stack
# 2: push -> direct prepend item to stack and then worry about adjusting old_max and max
# 3: pop -> directly pop, adjust stack and then worry about adjusting old_max and max
# 4: practice similar for get_min
# 5: For O(1) time and Constant space solution refer this :
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.old_max = None

class Stack:

	def __init__(self):
		self.stack = None
		self.max = None

	def push(self, data):
		n = Node(data)
		if self.stack == None:
			self.stack = n
		else:
			n.next = self.stack
			self.stack = n
		
		if self.max == None or n.data > self.max.data:
			n.old_max = self.max
			self.max = n

	def pop(self):
		if self.stack == None:
			raise Exception('Stack is null, can not pop')
		else:
			pop_item = self.stack
			self.stack = self.stack.next
			if pop_item.old_max != None:
				self.max = pop_item.old_max
				
			return pop_item.data

	def get_max(self):
		if self.stack == None:
			raise Exception('stack is empty so can not do max_stack')
		else:
			return self.max.data

s = Stack()
s.push(1)
print 'max is ' + str(s.get_max())
s.push(2)
print 'max is ' + str(s.get_max())
s.push(3)
print 'max is ' + str(s.get_max())
s.push(2)
print 'max is ' + str(s.get_max())
s.push(2)
print 'max is ' + str(s.get_max())
s.push(3)
print 'max is ' + str(s.get_max())


print(s.pop())
print 'max is ' + str(s.get_max())
print(s.pop())
print 'max is ' + str(s.get_max())
print(s.pop())
print 'max is ' + str(s.get_max())
print(s.pop())
print 'max is ' + str(s.get_max())
print(s.pop())
print 'max is ' + str(s.get_max())

