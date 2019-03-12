# https://www.geeksforgeeks.org/queue-using-stacks/

class MyQueue:

	def __init__(self):
		self.stack_en = []
		self.stack_de = []
		self.is_ok = False

	def _copy_stacks(self, src, des):
		while len(src) != 0:
			item = src.pop()
			des.append(item)

	def enqueue(self, data):
		if self.is_ok == False:
			self.stack_en.append(data)
		else:
			self._copy_stacks(self.stack_de, self.stack_en)
			self.stack_en.append(data)
			self.is_ok = False

	def dequeue(self):
		if self.is_ok == False:
			self._copy_stacks(self.stack_en, self.stack_de)
			self.is_ok = True
		
		if len(self.stack_de) == 0:
			raise Exception('Empty stack can not pop.')
		item = self.stack_de.pop()
		return item

q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print q.stack_en, q.stack_de

print(q.dequeue())
print(q.dequeue())
print q.stack_en, q.stack_de

q.enqueue(60)
q.enqueue(70)
print q.stack_en, q.stack_de

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print q.stack_en, q.stack_de

print(q.dequeue())
print(q.dequeue())
