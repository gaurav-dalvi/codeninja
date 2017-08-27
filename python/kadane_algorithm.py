# Write an efficient program to find the sum of contiguous subarray
# within a one-dimensional array of numbers which has the largest sum.
# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

def kadane_algorithm(arr):

    size = len(arr)
    max_sum = 0
    max_sum_so_far = 0

    for i in xrange(size):
        max_sum_so_far = max_sum_so_far + arr[i]
        if max_sum_so_far < 0:
            max_sum_so_far = 0
        if max_sum_so_far > max_sum:
            max_sum = max_sum_so_far

    return max_sum

if __name__ == '__main__':

    arr = [1,3,-2,-3,4,2,-5,1]
    print kadane_algorithm(arr)

    arr = [-2,-3,4,-1,-2,1,5,-3]
    print kadane_algorithm(arr)

    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print kadane_algorithm(arr)

    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print kadane_algorithm(arr)
