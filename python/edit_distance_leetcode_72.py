# https://www.geeksforgeeks.org/edit-distance-dp-5/
# https://leetcode.com/problems/edit-distance/
# https://www.youtube.com/watch?v=We3YDTzNXEk
# key is to think from the end of the string, otherwise becomes messy with indices of both string

def edit_distance_recursive(source, destination, m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if source[m-1] == destination[n-1]:
		return edit_distance_recursive(source, destination, m-1, n-1)
	else:
		delete_count = edit_distance_recursive(source, destination, m-1, n)
		replace_count = edit_distance_recursive(source, destination, m-1, n-1)
		insert_count = edit_distance_recursive(source, destination, m, n-1)
		return 1 + min(delete_count, replace_count, insert_count)

def edit_distance_dp(source, destination, m, n):
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif source[i-1] == destination[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], # delete
                                   dp[i-1][j-1], # replace
                                   dp[i][j-1]) # insert
	return dp[m][n]

source='rosrose'
destination='rose'
print(edit_distance_recursive(source, destination, len(source), len(destination)))
print(edit_distance_dp(source, destination, len(source), len(destination)))

source='sunday'
destination='saturday'
print(edit_distance_recursive(source, destination, len(source), len(destination)))
print(edit_distance_dp(source, destination, len(source), len(destination)))

source='geek'
destination='gesek'
print(edit_distance_recursive(source, destination, len(source), len(destination)))
print(edit_distance_dp(source, destination, len(source), len(destination)))


