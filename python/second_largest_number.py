def second_largest_number(arr):

    size = len(arr)
    if size < 2:
        print 'Invalid input'
        return

    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
    else:
        first = arr[1]
        second = arr[0]

    for i in xrange(2,size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] < first and arr[i] > second:
            second = arr[i]

    if first == second:
        print 'Can not find second largest'
        return

    return second


if __name__ == '__main__':

    arr = [5,3,7,1,3,9,4,7]
    print second_largest_number(arr)

    arr = [1,2,3,4,5,6,7,8,9]
    print second_largest_number(arr)

    arr = [1]
    print second_largest_number(arr)

    arr = [2,2,2,2]
    print second_largest_number(arr)
