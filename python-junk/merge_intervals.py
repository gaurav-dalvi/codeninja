# http://www.geeksforgeeks.org/merging-intervals/
#
# Given a set of time intervals in any order,
# merge all overlapping intervals into one and output the result
# which should have only mutually exclusive intervals.
# Let the intervals be represented as pairs of integers for simplicity.
# For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }.
# The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
# Similarly {5, 7} and {6, 8} should be merged and become {5, 8}

# adding +1 for start of interval and then adding -1 for end of interval. Sort it.
# When cumulative sum is zero, you have found interval
def merge_intervals_1(arr):

    temp_arr = []
    for item in arr:
        temp_arr.append((item[0], 1))
        temp_arr.append((item[1], -1))

    temp_arr = sorted(temp_arr,key=lambda x:x[0])
    result = []
    cum_sum = temp_arr[0][1]
    start_interval = temp_arr[0][0]
    for i in xrange(1, len(temp_arr)):
        cum_sum = cum_sum + temp_arr[i][1]
        if cum_sum == 0:
            end_interval = temp_arr[i][0]
            result.append((start_interval,end_interval))
            if (i+1) < len(temp_arr):
                start_interval = temp_arr[i+1][0]

    print result

# using stack to store intervals
def merge_intervals_2(arr):

    arr = sorted(arr, key=lambda x:x[0])
    stack = []
    # push first interval
    stack.append(arr[0])

    for i in xrange(1,len(arr)):

        top = stack.pop()
        stack.append(top) # peek operation

        if top[1] <= arr[i][0]:
            # no overlap, push on stack
            stack.append(arr[i])
        elif top[1] < arr[i][1]:
            top = (top[0], arr[i][1])
            stack.pop()
            stack.append(top)
    print stack

# inplace merging, no extra space
def merge_intervals_3(arr):

    arr = sorted(arr, key=lambda x: x[0])
    prev = arr[0]

    for i in xrange(1,len(arr)):

        # no overlap, move previous to current one
        if prev[1] <= arr[i][0]:
            prev = arr[i]
        elif prev[1] < arr[i][1]:
            # merging of two intervals
            temp = arr[i]
            new_tuple = (prev[0],arr[i][1])
            arr.remove(arr[i])
            arr.remove(prev)
            arr.insert(i-1,new_tuple)
        elif prev[0] > arr[i][0]:
            # discard arr element
            arr.remove(arr[i])



if __name__ == '__main__':
    # arr = [(1,3), (2,4), (5,7), (6,8)]
    # merge_intervals_1(arr)
    #
    # arr = [(1, 3), (6, 8)]
    # merge_intervals_1(arr)
    #
    # arr = [(1, 3), (3, 4)]
    # merge_intervals_1(arr)
    #
    # arr = [(1, 3), (1,3)]
    # merge_intervals_1(arr)
    #
    # arr = [(1, 4), (2,3), (4,6)]
    # merge_intervals_1(arr)
    #
    # print '------------------------'
    #
    # arr = [(1, 3), (2, 4), (5, 7), (6, 8)]
    # merge_intervals_2(arr)
    #
    # arr = [(1, 3), (6, 8)]
    # merge_intervals_2(arr)
    #
    # arr = [(1, 3), (3, 4)]
    # merge_intervals_2(arr)
    #
    # arr = [(1, 3), (1, 3)]
    # merge_intervals_2(arr)
    #
    # arr = [(1, 4), (2, 3), (4, 6)]
    # merge_intervals_2(arr)

    print '------------------------'

    arr = [(1, 3), (2, 4), (5, 7), (6, 8)]
    merge_intervals_3(arr)

    # arr = [(1, 3), (6, 8)]
    # merge_intervals_3(arr)
    #
    # arr = [(1, 3), (3, 4)]
    # merge_intervals_3(arr)
    #
    # arr = [(1, 3), (1, 3)]
    # merge_intervals_3(arr)
    #
    # arr = [(1, 4), (2, 3), (4, 6)]
    # merge_intervals_3(arr)