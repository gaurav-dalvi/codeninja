# Find top Kth largest element from the given array
# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

# 1: Sort and then return last K elements O(NlogN)
def solution1(arr, k):

    arr.sort(reverse=True)
    ans = []
    for i in xrange(k):
        ans.append(arr[i])
    return ans

# 2: Create temporary array and then do comparision using min_eleme in array method.
# O((n-k)*k)
def solution2(arr, k):

    ans = []
    min_element = arr[0]
    min_element_index = 0

    for i in xrange(k):
        ans.append(arr[i])

    min_element_index = find_min(ans)
    min_element = ans[min_element_index]

    for i in xrange(k, len(arr)):
        if arr[i] > ans[min_element_index]:
            ans.pop(min_element_index)
            ans.append(arr[i])
            min_element_index = find_min(ans)

    return ans


def find_min(arr):

    min_element = arr[0]
    min_element_index = 0
    for i in xrange(len(arr)):
        if arr[i] <= min_element:
            min_element = arr[i]
            min_element_index = i

    return min_element_index

def sol(arr, i, ans):
    if i == -1:
        return
    else:
        ans.append(arr[i])
        return sol(arr, i-1, ans)

if __name__ == '__main__':
    # arr = [12, 3, 5, 7, 1,12]
    # print solution1(arr, 2)

    arr = [12, 3, 5, 7, 1]
    print solution2(arr, 2)
