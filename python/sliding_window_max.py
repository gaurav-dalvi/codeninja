# Find max element in given window size for all elements in array
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# Key leanrings:
# 1: Store indices in queue (makes easy to find out of window element)
# 2: Learn about deque on python modeule of week

from collections import deque

def find_max_element_window(arr, k):

	# create deque
	q = deque()

	# fill deque and remove if incoming element is smaller that element in q
	for i in xrange(k):
		while q and arr[i] >= arr[q[-1]]:
			q.pop()
		q.append(i)

	# now process all other elements
	for i in xrange(k, len(arr)):

		# print max number from current window
		print arr[q[0]],

		# if number is out of window then remove it
		while q and q[0] <= i-k:
			q.popleft()
		# remove useless elements , exact same lines 16-18
		while q and arr[i] >= arr[q[-1]]:
			q.pop()
		q.append(i)

	# for last window
	print arr[q[0]]
if __name__ == '__main__':
	arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
	find_max_element_window(arr, 3)
	arr = [8,7,6,5,4,3,2,1]
	find_max_element_window(arr, 3)
