# https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/
# Given a number N, find the number of ways to represent this number as a sum of 2 or more consecutive natural numbers.

#Key Learnings:
# 1: No DP or nothing fancy, just pure maths
# 2: Why complexity is O(N^0.5)

def solution(N):

	count = 0
	L = 1
	while(L*(L+1) < 2*N):
		a = ((2.0 * N) - (L*L) - L) / (2*L + 2)
		if a - int(a) == 0.0: # if its integer
			count += 1
		L += 1
	return count

print solution(15) # ans is 3
print solution(10) # ans is 1
