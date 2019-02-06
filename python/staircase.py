# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
# https://www.youtube.com/watch?v=5o-kdjv7FD0&t=306s

def count_ways_r(n):
	if n == 0 or n == 1:
		return 1
	else:
		return count_ways_r(n-1) + count_ways_r(n-2)

def count_ways_dp(n):
	if n == 0 or n == 1:
		return 1
	arr = [0] * (n+1)
	arr[0] = 1
	arr[1] = 1
	for i in xrange(2, n+1):
		arr[i] = arr[i-1] + arr[i - 2]

	return arr[n]

def count_ways_r_1(n):
	if n < 0:
		return 0
	if n == 1 or n == 0:
		return 1
	else:
		total = 0
		for item in {1,3,5}:
			total += count_ways_r_1(n-item)
		return total

def count_ways_r_1_dp(n):
	if n < 0:
		return 0
	if n == 1 or n == 0:
		return 1
	arr = [0] * (n+1)
	arr[0] = arr[1] = 1
	for i in xrange(2,n+1):
		total = 0
		for item in {1,3,5}:
			if i - item >= 0:
				total += arr[i - item]
		arr[i] = total

	return arr[n]


print count_ways_r_1(0)
print count_ways_r_1(1)
print count_ways_r_1(2)
print count_ways_r_1(3)
print count_ways_r_1(4)
print "\n"
print(count_ways_r_1_dp(0))
print(count_ways_r_1_dp(1))
print(count_ways_r_1_dp(2))
print(count_ways_r_1_dp(3))
print(count_ways_r_1_dp(4))

