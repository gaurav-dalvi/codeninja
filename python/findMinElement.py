# http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
# with duplicates: https://www.programcreek.com/2014/03/leetcode-find-minimum-in-rotated-sorted-array-ii-java/
# Find minimum elelement from rotated sorted array

# Key Learnings:
# 1:To decide whether to left half of right half, always remember, lowest element will be in messed 
# up part of array. So check for that imbalance (arr[mid] > arr[low] or arr[mid] > arr[high])
# 2: Lowest element is the one whose previous element is greater that it
# 3: But in this case we need to check for (mid, mid -1) and (mid, mid+1) case
# THIS IS VERY important.
# 4: for duplicates its not possible to do this problem in O(log n) times.
# e.g: [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2] ,[2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2]


def get_min(arr, n):

    low = 0
    high = n-1

    while low <= high:

        mid = (high + low) / 2

        # decision criteria
        if mid > low and arr[mid] < arr[mid - 1]:
            return (arr[mid], mid)
        elif mid < high and arr[mid+1] < arr[mid]:
            return (arr[mid+1], mid+1)

        # left or right
        if arr[mid] < arr[low]:
            # left part
            high = mid - 1
        else:
            low = mid + 1

    if low > high:
        # not rotated at all
        return (arr[0], 0)

if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7,8]
    print get_min(arr, len(arr))

    arr = [8,1,2,3,4,5,6,7]
    print get_min(arr, len(arr))

    arr = [7,8,1,2,3,4,5,6]
    print get_min(arr, len(arr))

    arr = [6,7,8,1,2,3,4,5]
    print get_min(arr, len(arr))

    arr = [5,6,7,8,1,2,3,4]
    print get_min(arr, len(arr))

    arr = [4,5,6,7,8,1,2,3]
    print get_min(arr, len(arr))

    arr = [3,4,5,6,7,8,1,2]
    print get_min(arr, len(arr))

    arr = [2,3,4,5,6,7,8,1]
    print get_min(arr, len(arr))

    arr = [1]
    print get_min(arr, len(arr))

    arr = [2, 1]
    print get_min(arr, len(arr))

    arr = [1,2]
    print get_min(arr, len(arr))

    print '##############'
    arr = [1,1,3,4,4,5]
    print get_min(arr, len(arr))

    arr = [5,1,1,3,4,4]
    print get_min(arr, len(arr))

    arr = [4,5,1,1,3,4]
    print get_min(arr, len(arr))

    arr = [4,4,5,1,1,3]
    print get_min(arr, len(arr))

    arr = [3,4,4,5,1,1]
    print get_min(arr, len(arr))

    arr = [1,3,4,4,5,1]
    print get_min(arr, len(arr))

    arr = [2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2]
    print get_min(arr,len(arr))

    arr = [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2]
    print get_min(arr,len(arr))