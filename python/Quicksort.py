
def QuickSort(arr, first, last):
    if first < last:
        index = Partition(arr, first, last)

        QuickSort(arr, first, index - 1)
        QuickSort(arr, index + 1, last)

def Partition(arr, start, end):
    pivotElem = arr[start]
    pivotIndex = start
    start = start + 1
    done = False

    while not done:
        while start <= end and arr[start] <= pivotElem:
            start = start + 1
        while arr[end] >= pivotElem and end >= start:
            end = end - 1
        if end < start:
            done = True
        else:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]

    return end

if __name__ == '__main__':
    arr = [18,3,5,2,9,11,8]

    QuickSort(arr, 0, len(arr) - 1)
    print arr
