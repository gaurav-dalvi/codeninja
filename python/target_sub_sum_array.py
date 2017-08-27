# Find subarray with given sum | Set 1 (Nonnegative Numbers)
# Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.
#
# Examples:
#
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4
#
# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Ouptut: Sum found between indexes 1 and 4
#
# Input: arr[] = {1, 4}, sum = 0
# Output: No subarray found

# http://www.geeksforgeeks.org/find-subarray-with-given-sum/

def target_sum_sub_array(arr, sum):

    size = len(arr)
    curr_sum = arr[0]
    i = 1
    index = 0
    while i <= size:
        if curr_sum > sum:
            while(curr_sum > sum) and (index < i -1):
                curr_sum = curr_sum - arr[index]
                index = index + 1
        if sum == curr_sum:
            ans = (index,i-1)
            return ans
        if i < size:
            curr_sum = curr_sum + arr[i]
        i = i + 1

    print 'no subarray found'
    return tuple()

if __name__ == '__main__':
    arr = [1,4,20,3,10,5]
    ans = target_sum_sub_array(arr, 33)
    print ans

    arr = [1, 4, 0, 0, 3, 10, 5]
    ans = target_sum_sub_array(arr, 7)
    print ans

    arr = [1,4]
    ans = target_sum_sub_array(arr, 0)
    print ans

    arr = [1,4,3]
    ans = target_sum_sub_array(arr, 8)
    print ans
