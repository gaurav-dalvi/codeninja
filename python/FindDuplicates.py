# Given an array of intergers where each value 1<=x<=(len(array))
# Find all duplicates in that array
# inp = [1,2,1,2]
# oup = [1,2]
# https://www.youtube.com/watch?v=GeHOlt_QYz8&t=5s
# Time Complexity : O(n)
# Space Complexity: O(1)

def findDuplicates(arr):
    ans = set()

    if arr is not None and len(arr) > 0:
        for i in xrange(len(arr)):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                # duplicate found
                ans.add(abs(arr[i]))
            else:
                arr[index] = (-1) * arr[index]

    return ans


if __name__ == '__main__':

    arr = None
    ans = findDuplicates(arr)
    print ans

    arr = []
    ans = findDuplicates(arr)
    print ans

    arr = [1,2,3,4]
    ans = findDuplicates(arr)
    print ans

    arr = [1,1,1]
    ans = findDuplicates(arr)
    print ans

    arr = [1,2,1,2]
    ans = findDuplicates(arr)
    print ans

    arr = [1,4,3,1]
    ans = findDuplicates(arr)
    print ans
