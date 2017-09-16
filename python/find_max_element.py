
# http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
# https://www.programcreek.com/2014/02/leetcode-find-minimum-in-rotated-sorted-array/
# Find maximum elelement from rotated sorted array

# Following Cases

# 1: if arr[low] < arr[high] -- array is not rotated at all
# 2: if high == low -- if array has just one element
# 3: check if mid-1 is maximum element
# 4: check if mid is maximum elment
# 4: then do binary search left or right




def find_max_element(arr):

    low = 0
    high = len(arr) - 1

    # if only one element is left
    if high == low:
        return arr[high]

    # if array is not rotated at all
    if arr[low] < arr[high]:
        return arr[high]

    while low < high:

        mid = low + (high - low) / 2

        # if mid is high
        if mid < high and arr[mid+1] < arr[mid]:
            return arr[mid]
        # if mid - 1 high
        elif mid > low and arr[mid-1] > arr[mid]:
            return arr[mid - 1]
        else:
            if arr[mid] < arr[high]:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print 'max element: %s' % find_max_element(arr)

    arr = [3, 4, 5, 6, 7, 1, 2]
    print 'max element: %s' % find_max_element(arr)

    arr = [7, 1, 2, 3, 4, 5, 6]
    print 'max element: %s' % find_max_element(arr)

    arr = [1, 2, 3, 4]
    print 'max element: %s' %find_max_element(arr)

    arr = [1]
    print 'max element: %s' % find_max_element(arr)

    arr = [1,2]
    print 'max element: %s' % find_max_element(arr)

    arr = [3,4,5,1,2]
    print 'max element: %s' % find_max_element(arr)

    arr = [2, 1]
    print 'max element: %s' % find_max_element(arr)
