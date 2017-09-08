# Count number of occurrences (or frequency) in a sorted array
# Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. 
# Expected time complexity is O(Logn)
# http://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

def first(arr, low, high, key):

    if low <= high:

        mid = low + (high - low)/2

        if (mid == 0 or arr[mid-1] < key) and arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return first(arr,mid+1, high, key)
        else:
            return first(arr, low, mid-1, key)

    return -1

def last(arr, low, high, key):

    if low <= high:

        mid = low + (high - low)/2

        if (mid == high or arr[mid + 1] > key) and arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return last(arr,low, mid-1, key)
        else:
            return last(arr, mid+1, high, key)

    return -1

def freq_count_binary_search(arr, low, high, key):

    start_index = first(arr, low, high, key)
    end_index = last(arr, low, high, key)

    if start_index == -1:
        return start_index

    return end_index - start_index + 1

if __name__ == '__main__':

    arr = [1,2,2,3,3,3,3]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 3)

    arr = [1,1,1,1,1,1]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 1)

    arr = [1, 1, 1, 1, 1, 1]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 2)

    arr = [1,2,3,4,5,6]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 1)

    arr = [1, 2, 3, 4, 5, 6]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 6)

    arr = [1, 2, 3, 4, 5, 6]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 4)

    arr = [1, 2, 3, 4, 5, 6]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 7)

    arr = [1,1,1,2,3,4,5,6,7,8]
    print freq_count_binary_search(arr, 0, len(arr) - 1, 1)
