def SmallLargeMerge(smallArr, largeArr):
    #Move array
    largeArr.reverse()
    largeArr.sort()
    smallIndex = 0
    midIndex = len(smallArr) - 1
    for i in xrange(len(largeArr)):

        if smallArr[index] > largeArr[midIndex]:

if __name__ == '__main__':
    smallArr = [3,6,8,11]
    largeArr = [1,6,10,15,0,0,0,0]
    SmallLargeMerge(smallArr, largeArr)