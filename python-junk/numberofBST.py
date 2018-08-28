def numBST(keys):
    if keys <= 1:
        return 1
    else:
        sum = 0
        left = right = 0
        for i in xrange(1,keys+1):
            left = numBST(i - 1)
            right = numBST(keys - i)
            sum = sum + left * right
    return sum

if __name__ == '__main__':
    print numBST(5)