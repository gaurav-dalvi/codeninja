# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# https://www.ideserve.co.in/learn/maximum-element-from-each-subarray-of-size-k-set-2
# 1: You need to first process k elements and then drive main logic, otherwise I was stuck to do eveything in one for loop
# 2: Need to solve this problem in less than 20 mins , full code with no bugs
# 3: Implement your own dequeu


from collections import deque

def max_from_each_sub_array(array, window_size):

    if array is None:
        raise Exception('Invalid Input')
        return
    q = deque()
    size = len(array)
    op = []

    for i in xrange(window_size):

        # if incoming element is greater than rear end of queue then
        # current element in the queue is useless so remove it
        while q and array[i] >= array[q[-1]]:
            q.pop()
        # add element in queue
        q.append(i)

    # remaining processing
    for i in xrange(window_size,size):

        # add first element of queue in the o/p
        op.append(array[q[0]])

        # evict element from q if its outside of current window
        while q and q[0] <= i - window_size:
            # pop from left i.e: front end of queue
            q.popleft()

        # if incoming element is greater that rear end of queue then
        # current element in the queue is useless so remove it
        while  q and array[i] >= array[q[-1]]:
            q.pop()

        q.append(i)

    op.append(array[q[0]])
    return op

if __name__ == '__main__':
    arr = [9,6,11,8,10,5,14,13,93,14]
    print max_from_each_sub_array(arr, 4)

    arr = [12, 1, 78, 90, 57, 89, 56]
    print max_from_each_sub_array(arr, 3)

    arr = [1,2,3,4,5,6,7,8,9]
    print max_from_each_sub_array(arr, 4)

    arr = [9,8,7,6,5,4,3,2,1]
    print max_from_each_sub_array(arr, 4)

    arr = [1,1,1,1,1,1,1,1]
    print max_from_each_sub_array(arr, 1)

    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    print max_from_each_sub_array(arr, 2)
