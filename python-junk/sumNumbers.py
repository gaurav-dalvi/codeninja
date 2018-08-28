def findMissingNumber(intArr):

    totalSum = 0
    for i in xrange(len(intArr)):
        totalSum = totalSum + intArr[i]

    n = len(intArr) + 1
    realSum = (n * (n + 1)) / 2

    return (realSum - totalSum)


if __name__ == '__main__':
    print findMissingNumber([4,2,1,3,5])