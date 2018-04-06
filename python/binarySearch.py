# Implement Binary search.
# Key Learnings : 
# 1: codition is always low <= high and NOT low < high
# 2: high is always started with len(arr) - 1 , -1 because it directly access array by that index

def bin_search(arr, key):

    high = len(arr)-1
    low = 0
    while low <= high:
        mid = (low+high)/2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

def bin_search_1(arr, key, low,high):

    if low <= high:
        mid = (high + low) /2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            return bin_search_1(arr, key, low, mid - 1)
        else:
            return bin_search_1(arr,key, mid +1, high)
    return False


if __name__ == '__main__':
    arr = [1,2,3,4,5,6]

    print bin_search(arr, -1)
    print bin_search(arr, 1)
    print bin_search(arr, 2)
    print bin_search(arr, 3)
    print bin_search(arr, 4)
    print bin_search(arr, 5)
    print bin_search(arr, 6)
    print bin_search(arr, 7)
    print '\n'

    print bin_search_1(arr, -1, 0, len(arr)-1)
    print bin_search_1(arr, 1, 0, len(arr) - 1)
    print bin_search_1(arr, 2, 0, len(arr) - 1)
    print bin_search_1(arr, 3, 0, len(arr) - 1)
    print bin_search_1(arr, 4, 0, len(arr) - 1)
    print bin_search_1(arr, 5, 0, len(arr) - 1)
    print bin_search_1(arr, 6, 0, len(arr) - 1)
    print bin_search_1(arr, 7, 0, len(arr) - 1)
