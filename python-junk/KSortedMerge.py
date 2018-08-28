# Merge K sorted arrays.
#
# Repeats are allowed
# Negative numbers and zeros are allowed
# Optimal Solution O(NKlogN)
# N = Length of each Array
# K = Number of Arrays

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, 0)

def FindMin(arr):
    tempTuple = arr[0]
    minimum = (tempTuple[0], tempTuple[1])
    for i in arr:
        if i[0] < minimum[0]:
            minimum = (i[0], i[1])

    return minimum

def mergeArrays(arr, k, n):

    ans = []
    tempArr = [0] * k
    for i in xrange(k):
        tempArr[i] = (arr[i][0], 0)

    for i in xrange(k*n):
        temp = FindMin(tempArr)
        ans.append(temp[0])
        arrIndex = tempArr.index(temp)
        newCount = temp[1] + 1
        temp = (arr[arrIndex][newCount],newCount)

        temp.

    return ans



if __name__ == '__main__':
    arr = [[1,3,5,7],[2,4,6,8],[0,9,10,11]]
    op = mergeArrays(arr)
    print op