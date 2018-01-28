# https://www.ideserve.co.in/learn/find-the-missing-number-in-the-increasing-sequence
# key learning : line 17 is NOT high = mid - 1
# O(log n)
def find_missing_number_binary_search(arr):

    if arr is None:
        raise Exception('Invalid Input')

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = ( low + high ) /2
        if low == high:
            return arr[high] - 1
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid

if __name__ == '__main__':

    arr = [1,2,4,5,6,7,8]
    print find_missing_number_binary_search(arr)

    arr = [1,2,3,4,6,7,8]
    print find_missing_number_binary_search(arr)

    arr = [2,3,4,5,6]
    print find_missing_number_binary_search(arr)
