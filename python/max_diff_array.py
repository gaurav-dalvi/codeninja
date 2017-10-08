# Maximum difference between two elements such that larger element appears after the smaller number
# Given an array arr[] of integers, find out the difference between any two elements such that larger element
# appears after the smaller number in arr[].
#
# Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8
# (Diff between 10 and 2). If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)

def solution1(arr):

    # O(n2) solution
    max_diff = -1
    size = len(arr)

    for i in xrange(size):
        for j in xrange(i,size):

            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]

    return max_diff

def solution2(arr):
    # O(n) space and time
    # keep track of max_diff so far and min_element so far

    max_diff = -1
    min_number = arr[0]

    for i in xrange(1,len(arr)):
        if arr[i] - min_number > max_diff:
           max_diff = arr[i] - min_number
        if min_number > arr[i]:
            min_number = arr[i]

    return max_diff

def solution3(arr):

    # O(n) time and space
    # keep track of right_max element and max_diff element
    # traverse array backwards
    max_diff = -1
    max_element = arr[len(arr) - 1]
    for i in xrange(len(arr) -2, -1,-1):
        if arr[i] > max_element:
            max_element = arr[i]
        else:
            diff = max_element - arr[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff

if __name__ == '__main__':

    arr =  [2, 3, 10, 6, 4, 8, 1]
    print solution3(arr)

    arr = [7,9,5,6,3,2]
    print solution3(arr)

    arr = [1,2,6,80,100]
    print solution3(arr)

    arr = [80,2,6,3,100]
    print solution3(arr)
