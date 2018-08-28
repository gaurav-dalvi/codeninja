def checkValid(arr, k):
    for i in xrange(k):
        ci = i
        ri = arr[i]
        ck = k
        rk = arr[k]
        if abs(ci-ck) == abs(ri-rk):
            return False
    return True

def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]

def placeNQueens(arr, index):
    if index == len(arr):
        print arr
        return True
    else:
        for i in xrange(len(arr)):
            swap(arr, i, index)
            if checkValid(arr, index) == True:
                placeNQueens(arr, index+1)
                return True
            swap(arr, i, index)

    return False

if __name__ == '__main__':
    nQueens = 5
    a = [None] * nQueens
    for i in xrange(nQueens):
        a[i] = i
    placeNQueens(a, 0)
