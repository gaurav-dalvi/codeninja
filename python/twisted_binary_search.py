# Search element in sorted but rotated bytearray
# http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# Helper function
def binary_search(arr, low, high, key):

    if high < low:
        return -1

    mid = low + (high - low )/2
    if arr[mid] == key:
        return mid
    else:
        if key < arr[mid]:
            # left half
            return binary_search(arr, low, mid -1, key)
        else:
            return binary_search(arr, mid+1,high, key)

# helper function
# Function to get pivot. For array
#        3, 4, 5, 6, 1, 2 it returns
#        3 (index of 6)
def find_pivot(arr):

    low = 0
    high = len(arr) - 1

    # if only one element is left
    if high == low:
        return low

    # if array is not rotated at all
    if arr[low] < arr[high]:
        return -1

    while low < high:

        mid = low + (high - low) / 2

        # if mid is high
        if mid < high and arr[mid+1] < arr[mid]:
            return mid
        # if mid - 1 high
        elif mid > low and arr[mid-1] > arr[mid]:
            return (mid-1)
        else:
            if arr[mid] < arr[high]:
                high = mid - 1
            else:
                low = mid + 1

def search_element(arr, key):

    if arr is None:
        return False
    low = 0
    high = len(arr) - 1

    if arr[low] < arr[high]:
        # array is not rotated
        return binary_search(arr, low, high, key)
    else:
        index = find_pivot(arr)
        if arr[index] == key:
            return index
        elif arr[0] <= key:
            # left half
            return binary_search(arr, low, index-1, key)
        else:
            return binary_search(arr, index+1, high,key)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    key = 2
    print search_element(arr,key)

    arr = [3, 4, 5, 6, 7, 1, 2]
    key = 2
    print search_element(arr, key)

    arr = [7, 1, 2, 3, 4, 5, 6]
    key = 2
    print search_element(arr, key)

    arr = [1, 2, 3, 4]
    key = 2
    print search_element(arr, key)

    arr = [1]
    key = 2
    print search_element(arr, key)

    arr = [1,2]
    key = 2
    print search_element(arr, key)

    arr = [3,4,5,1,2]
    key = 2
    print search_element(arr, key)

    arr = [2, 1]
    key = 2
    print search_element(arr, key)
