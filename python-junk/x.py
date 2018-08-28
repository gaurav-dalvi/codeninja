
# http://www.geeksforgeeks.org/heap-sort/

def heapify(arr, size, i):
    left = (i * 2) + 1
    right = (i * 2) + 2
    largest = i

    if left < size and arr[left] >= arr[largest]:
        largest = left

    if right < size and arr[right] >= arr[largest]:
        largest = right

    # if children is greater than parent, then swap and call hepify in recursion
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,size, largest)

def heapsort(arr):
    if arr is not None:
        size = len(arr)
        for i in xrange(size-1,-1,-1):
            heapify(arr, size, i)
        # heapify(arr,size,0)

        # extract first element of the array and swap it with last one.
        # rehepify again for reduced size of array
        for i in xrange(size-1, -1,-1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i,0)


if __name__ == '__main__':

    # arr = [8,3,6,1,10,12,4,3,-1, 18,15,1]
    # heapsort(arr)
    # print arr

    arr = [1,2,3,4,5,6]
    heapsort(arr)
    print arr

    # arr = [6,5,4,3,2,1]
    # heapsort(arr)
    # print arr
    #
    # arr = [1,1,1,1,1]
    # heapsort(arr)
    # print arr
    #
    # arr = []
    # heapsort(arr)
    # print arr
    #
    # arr = None
    # heapsort(arr)
    # print arr
    #
    # arr = [4,10,3,5,1]
    # heapsort(arr)
    # print arr