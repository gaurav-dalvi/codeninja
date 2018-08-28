import sys

def maxDegree(map):
    degree = 0
    for i in map.keys():
        if map[i] > degree:
            degree = map[i]
    return degree


def freqCount(arr):
    map = {}
    for i in arr:
        if i not in map.keys():
            map[i] = 1
        else:
            count = map[i]
            map[i] = count + 1
    return map


def degreeOfArray(arr):
    map = freqCount(arr)

    if map is None:
        return 0

    ans = sys.maxint
    degree = maxDegree(map)
    j = degree

    while j < len(arr) + 1:
        for i in xrange(0, len(arr) - j + 1):
            subArr = arr[i: i + j]
            map = freqCount(subArr)
            curr_degree = maxDegree(map)
            if curr_degree == degree:
                if len(subArr) < ans:
                    ans = len(subArr)
        j = j + 1
    return ans

if __name__ == '__main__':
    # FreqCount([1,1,2,1,2,2,4])
    arr = [1,2,2,3,1]
    print degreeOfArray(arr)
