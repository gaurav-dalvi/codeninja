max_sum = 0

def solution(arr, i, X, Y):
    global max_sum

    if i >= len(arr):
        return
    else:

        X.append(a[i])
        solution(arr, i+1, X, Y)

        X1 = sum(X)
        Y1 = sum(Y)
        if (X1 == Y1) and max_sum < X1:
            max_sum = X1
        X.remove(a[i])

        Y.append(a[i])
        solution(arr, i+1, X, Y)
        X1 = sum(X)
        Y1 = sum(Y)

        if (X1 == Y1) and max_sum < X1:
            max_sum = X1
        Y.remove(a[i])

if __name__ == '__main__':
    max_sum = 0
    a = [4,18,22,10,4]
    X = list()
    Y = list()
    solution(a, 0, X, Y)
    print max_sum


