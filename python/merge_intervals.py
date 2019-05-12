# Key Learnins:
# https://www.geeksforgeeks.org/merging-intervals/
# How to sort list of tuples : https://stackoverflow.com/a/3121985
# https://www.geeksforgeeks.org/merging-intervals/
# See how case of (1,10) and (3,5) is automatically handled, we dont add 
# it to stack

# stack based solution, extra space
def merge_intervals_1(intervals):

	# sort based on start of the interval
	intervals = sorted(intervals, key=lambda tup: tup[0])
	stack = []
	stack.append(intervals[0])
	for i in xrange(1, len(intervals)):
		top = stack[-1]
		if top[1] < intervals[i][0]:
			# no overlap
			stack.append(intervals[i])
		elif top[1] < intervals[i][1]:
			# overlap
			new_interval = (top[0], intervals[i][1])
			stack.pop()
			stack.append(new_interval)
	return stack

def merge_intervals_2(intervals):

	# sort in ascending order
	intervals = sorted(intervals, key=lambda tup: tup[0], reverse = True)
	index = 0
	for i in xrange(len(intervals)):
		if i != 0 and intervals[index-1][0] <= intervals[i][1]:
			while index != 0 and intervals[index-1][0] <= intervals[i][1]:
				intervals[index - 1] = (min(intervals[index-1][0], intervals[i][0]), max(intervals[index-1][1], intervals[i][1]))
				index -= 1
		else:
			intervals[index] = intervals[i]
		index += 1

	return intervals[:index]
intervals = [(2,4), (5,7), (6,8), (1,3)]
print merge_intervals_2(intervals)

intervals = [(1,10), (3,5)]
print merge_intervals_2(intervals)

intervals = [(1,9), (2,4), (6,8), (4,7)]
print merge_intervals_2(intervals)
