def MyMerge(inp, leftArrayBegin, rightArrayBegin, rightArrayEnd):
    solution = [0] * (rightArrayEnd - leftArrayBegin + 1)
    leftArrayEnd = rightArrayBegin - 1
    index = 0

    while (leftArrayBegin <= leftArrayEnd) and (rightArrayBegin <= rightArrayEnd):
        if inp[leftArrayBegin] <= inp[rightArrayBegin]:
            solution[index] = inp[leftArrayBegin]
            index = index + 1
            leftArrayBegin = leftArrayBegin + 1
        else:
            solution[index] = inp[rightArrayBegin]
            index = index + 1
            rightArrayBegin = rightArrayBegin + 1

    # if left array has still elements then copy over solution array
    while leftArrayBegin <= leftArrayEnd:
        solution[index] = inp[leftArrayBegin]
        index = index + 1
        leftArrayBegin = leftArrayBegin + 1

    # if right array has still elements then copy over solution array
    while rightArrayBegin <= rightArrayEnd:
        solution[index] = inp[rightArrayBegin]
        index = index + 1
        rightArrayBegin = rightArrayBegin + 1

    # Copy solution array back to input array now:
    for i in xrange(len(solution)-1,-1,-1):
        inp[rightArrayEnd] = solution[i]
        rightArrayEnd = rightArrayEnd -1

    print '###',inp

def MyMergeSort(inp, low, high):
    if low < high:
        mid = (low + high) / 2
        MyMergeSort(inp, low, mid)
        MyMergeSort(inp, mid + 1, high)
        # Merge the results
        MyMerge(inp, low, mid + 1, high)


def MergeSort(intArr):
    high = len(intArr)
    MyMergeSort(intArr, 0, high - 1)
    return intArr

if __name__ == '__main__':

    inputArr = [3,4,1,6,9,22,4,10,2]
    MergeSort(inputArr)
    print inputArr
