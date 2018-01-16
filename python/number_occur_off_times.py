# Problem: http://www.ideserve.co.in/learn/find-the-number-which-occurs-odd-number-of-times

def number_occur_odd_times_1(arr):
	size = len(arr)
	count_map = {}
	for num in arr:
		if num in count_map.keys():
			temp = count_map[num]
			count_map[num] = temp + 1
		else:
			count_map[num] = 1

	for k,v in count_map.items():
		if v % 2 == 1:
			return k

	return 0

# do XOR
def number_occur_odd_times_2(arr):
	size = len(arr)

	result = arr[0]
	for i in xrange(1,size):
		result = result ^ arr[i]
	return result


if __name__ == '__main__':
	arr = [2,5,9,1,5,1,8,2,8]
	print number_occur_odd_times_1(arr)

	arr = [2,3,4,3,1,4,5,1,2,4,5]
	print number_occur_odd_times_1(arr)

	arr = [2,5,9,1,5,1,8,2,8]
	print number_occur_odd_times_2(arr)

	arr = [2,3,4,3,1,4,5,1,2,4,5]
	print number_occur_odd_times_2(arr)
