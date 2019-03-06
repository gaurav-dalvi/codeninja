# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
# Go for optimized approach.
# What to do with duplicatem in elements.

class Stack:

	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, data):
		if len(self.stack) == 0:
			self.stack.append(data)
			self.min_stack.append(data)
		else:
			self.stack.append(data)
			if self.min_stack[len(self.min_stack) - 1] >= data:
				self.min_stack.append(data)

	def pop(self):
		if len(self.stack) == 0:
			raise Exception('Empty stack, pop operation not permitted')
		pop_item = self.stack.pop()
		if pop_item == self.min_stack[len(self.min_stack) - 1]:
			self.min_stack.pop()
		return pop_item

	def get_min(self):
		if len(self.stack) == 0:
			raise Exception('Empty stack, get_min operation not permitted')
		else:
			return self.min_stack[len(self.min_stack) - 1]

s = Stack()
s.push(18)
print s.stack, s.min_stack
print s.get_min()

s.push(19)
print s.stack, s.min_stack
print s.get_min()

s.push(29)
print s.stack, s.min_stack
print s.get_min()

s.push(15)
print s.stack, s.min_stack
print s.get_min()

s.push(16)
print s.stack, s.min_stack
print s.get_min()

s.push(1)
print s.stack, s.min_stack
print s.get_min()

print s.pop(), s.get_min()
print s.pop(), s.get_min()
print s.pop(), s.get_min()
print s.pop(), s.get_min()
print s.pop(), s.get_min()
print s.pop()
