# Given an array, print all subarrays in the array which has sum 0.
#
# Input:  arr = [6, 3, -1, -3, 4, -2, 2,
#              4, 6, -12, -7]
# Output:
# Subarray found from Index 2 to 4
# Subarray found from Index 2 to 6
# Subarray found from Index 5 to 6
# Subarray found from Index 6 to 9
# Subarray found from Index 0 to 10
# http://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/


def sum_zero_solution(arr):

    size = len(arr)
    map = {}
    sum = 0
    ans = []
    # if subarray with sum zero starts with zero index
    map[0] = [-1]

    for i in xrange(size):
        sum = sum + arr[i]
        if map.has_key(sum):
            temp_list = map[sum]
            for j in temp_list:
                ans.append((j+1, i))

        if map.has_key(sum):
            curr_list = map[sum]
            curr_list.append(i)
            map[sum] = curr_list
        else:
            map[sum] = [i]

    for i in ans:
        print i

if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2, 2 ,4, 6, -12, -7]
    sum_zero_solution(arr)
    print '###############'

    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    sum_zero_solution(arr)
