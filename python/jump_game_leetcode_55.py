# https://leetcode.com/problems/jump-game/

def jump_game_recursive(index, arr):
	if index == len(arr) - 1:
		return True
	steps = min(index + arr[index], len(arr)-1)
	for i in range(index+1, steps+1):
		if jump_game_recursive(i, arr):
			return True
	return False

# this is just memorization on the top of recursive solution
def jump_game_top_to_bottom_dp(index, arr, memo):
	if memo[index] != 0:
		if memo[index] == 1:
			return True
		return False
	steps = min(index + arr[index], len(arr) - 1)
	for i in range(index+1, steps+1):
		if jump_game_top_to_bottom_dp(i, arr, memo):
			memo[i] = 1
			return True
	memo[index] = 2
	return False

def jump_game_bottom_to_top_dp(index, arr):
	memo = [0] * len(arr)
	memo[len(arr) - 1] = 1
	for i in range(len(arr) - 2, -1, -1):
		farthest_jump = min(i+ arr[i], len(arr)-1)
		for j in range(i+1, furthest_jump+1):
			if memo[j] == 1:
				memo[i] = 1
				break
	if memo[0] == 0:
		return False
	return True
			
# nums = [2,3,1,1,4]
# print(jump_game_recursive(0, nums))

# nums = [3,2,1,0,4]
# print(jump_game_recursive(0, nums))

# nums = [2,3,1,1,4]
# memo = [0] * len(nums)
# memo[len(nums) - 1] = 1
# print(jump_game_top_to_bottom_dp(0, nums, memo))

# nums = [3,2,1,0,4]
# memo = [0] * len(nums)
# memo[len(nums) - 1] = 1
# print(jump_game_top_to_bottom_dp(0, nums, memo))

nums = [2,3,1,1,4]
print(jump_game_bottom_to_top_dp(0, nums))

nums = [3,2,1,0,4]
print(jump_game_bottom_to_top_dp(0, nums))
