# https://www.youtube.com/watch?v=qH7fVuYlOOc
# Given a sum and coins find minimum number of coins needed to get to the sum
# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
# Base state is : to get sum as 0 we need 0 coins
# Then to for all next sums above 0, we need to check for all the coins which are less than sum-coinValue
# Then for each of that value, add 1 (because of new case) and then find minimum of all of them and 
# then store it in optimal_solution array
import sys

def coin_select_dp(coins, target_sum):

	sub_solution = [sys.maxint for i in xrange(target_sum+1)]
	sub_solution[0] = 0

	for i in xrange(1,target_sum+1): # iterate for all the sum from 1 to target_sum
		for j in xrange(len(coins)): # iterate over all coins
			if coins[j] <= i: # check for only coins that can lead us to optimal solution for current sum = i
				temp = sub_solution[i - coins[j]] # get previous optimal_solution
				if temp != sys.maxint and temp +1 < sub_solution[i]: # check min
					sub_solution[i] = temp + 1
	
	# print sub_solution
	print sub_solution[target_sum]

def coin_select_recur(coins, target_sum):

	if target_sum <= 0:
		return 0
	opt_min = target_sum
	for coin in coins:
		if target_sum - coin >= 0:
			count = coin_select_recur(coins, target_sum - coin)
			if count + 1 < opt_min:
				opt_min = count + 1

	return opt_min

def internal(coins, target_sum, solution):
	if target_sum == 0:
		return 0
	
	opt_min = target_sum
	for coin in coins:
		if target_sum - coin >= 0:
			c = 0
			if solution[target_sum - coin] >= 0:
				c = solution[target_sum - coin]
			else:
				c = internal(coins, target_sum - coin, solution)
				solution[target_sum - coin] = c
			if opt_min > c + 1: opt_min = c + 1

	return opt_min


def coin_select_dp_1(coins, target_sum):
	solution = [-1 for i in xrange(target_sum + 1)]
	return internal(coins, target_sum, solution)


if __name__ == '__main__':

	coins = [1,3,5]
	coin_select_dp(coins, 11)
	print coin_select_recur(coins, 11)
	print coin_select_dp_1(coins, 11)

	coins = [25,10,5]
	coin_select_dp(coins, 30)
	print coin_select_recur(coins, 30)
	print coin_select_dp_1(coins, 30)

	coins = [9, 6, 5, 1]
	coin_select_dp(coins, 13)
	print coin_select_recur(coins, 13)
	print coin_select_dp_1(coins, 13)
