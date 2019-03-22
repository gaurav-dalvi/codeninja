# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
# this can be used to design quick own priority queue. Focus on MaxHeapObject class

import heapq

class MinHeap:

	def __init__(self):
		self.list = []
	
	def heappush(self, data):
		heapq.heappush(self.list, data)
	
	def heappop(self):
		if len(self.list) == 0:
			raise Exception('heap is empty, can not pop')
		item = heapq.heappop(self.list)
		return item

class MaxHeapObject:

	def __init__(self, val):
		self.val = val
	def __lt__(self, new_obj):
		return self.val > new_obj.val
	def __eq__(self, new_obj):
		return self.val == new_obj.val


class MaxHeap:

	def __init__(self):
		self.list = []

	def heappush(self, val):
		heapq.heappush(self.list, MaxHeapObject(val))

	def heappop(self):
		if len(self.list) == 0:
			raise Exception('Can not pop from the empty heap')
		item = heapq.heappop(self.list)
		return item.val

def test_min_heap():
	h = MinHeap()
	h.heappush(10)
	h.heappush(15)
	h.heappush(9)
	h.heappush(2)
	h.heappush(5)
	h.heappush(7)
	print h.list

	print h.heappop()
	print h.list

	print h.heappop()
	print h.list

	print h.heappop()
	print h.list

	print h.heappop()
	print h.list

	print h.heappop()
	print h.list

	print h.heappop()
	print h.list

def test_max_heap():
	
	h = MaxHeap()
	h.heappush(10)
	h.heappush(15)
	h.heappush(9)
	h.heappush(2)
	h.heappush(5)
	h.heappush(7)

	print h.heappop()
	print h.heappop()
	print h.heappop()
	print h.heappop()
	print h.heappop()
	print h.heappop()

test_max_heap()
