# https://www.ideserve.co.in/learn/last-index-of-element-in-sorted-array-with-duplicates
# Key points :
#   No need to over complicate
#   Key thing is if arr[mid+1] > target thats the case to stop or arr[mid-1]<target in any of the case
#   how not to return directly from inside for loop : good practice
#   Focus on how you have implemented this in only 2 if else conditions. Better and clean code practice.

# last matching element's index
def find_last_index_duplicate_BST(arr, target):

    if arr is None:
        raise Exception("Invalid Input")

    ret_index = -1

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high-low)/2
        if (arr[mid] == target) and ((mid == high) or (arr[mid+1] > target)):
            ret_index = mid
            break
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return ret_index

# first matching element's index
def find_first_index_duplicate_BST(arr, target):

    if arr is None:
        raise Exception("Invalid Input")

    ret_index = -1

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high-low)/2
        if arr[mid] == target and ((mid == low) or (arr[mid-1] < target)):
            ret_index = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ret_index

if __name__ == '__main__':

    arr = [0,1,2,2,4,5,5,5,8]
    print find_last_index_duplicate_BST(arr, 5)

    arr = [3,3,5,6,7,7,7,8,9,10]
    print find_last_index_duplicate_BST(arr, 5)

    arr = [3,4,5,6,7]
    print find_last_index_duplicate_BST(arr, 5)

    arr = [3, 4, 5, 6, 7]
    print find_last_index_duplicate_BST(arr, 8)

    arr = [5,5,5,6,7,8,9]
    print find_last_index_duplicate_BST(arr, 5)

    arr = [1,2,3,4,5,5,5,5]
    print find_last_index_duplicate_BST(arr, 5)
    print

    arr = [0, 1, 2, 2, 4, 5, 5, 5, 8]
    print find_first_index_duplicate_BST(arr, 5)

    arr = [3, 3, 5, 6, 7, 7, 7, 8, 9, 10]
    print find_first_index_duplicate_BST(arr, 5)

    arr = [3, 4, 5, 6, 7]
    print find_first_index_duplicate_BST(arr, 5)

    arr = [3, 4, 5, 6, 7]
    print find_first_index_duplicate_BST(arr, 8)

    arr = [5, 5, 5, 6, 7, 8, 9]
    print find_first_index_duplicate_BST(arr, 5)

    arr = [1, 2, 3, 4, 5, 5, 5, 5]
    print find_first_index_duplicate_BST(arr, 5)
