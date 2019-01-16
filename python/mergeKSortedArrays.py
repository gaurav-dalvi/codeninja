import heapq
def merge(arr):

	output = []
	li = []
	heapq.heapify(li)
	# push first elements from all arrays into heapq
	for i in xrange(len(arr)):
		heapq.heappush(li, [arr[i][0], i, 0])

	while len(li) != 0:
		output.append(li[0][0])
		elem = heapq.heappop(li)

		arr_index = elem[1]
		elem_index = elem[2]
		if elem_index + 1 < len(arr[elem[1]]):
			heapq.heappush(li, [arr[arr_index][elem_index+1], arr_index, elem_index+1])

	return output

arr = [[1,3,4],
	   [2,5,6],
	   [0,9,10,11]]
