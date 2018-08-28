def rotate(inp):
    size = len(inp)
    temp = inp[0]
    temp1 = ''
    i = 1
    k = 0
    while i < size:
        temp1 = inp[i]
        inp[k] = temp1
        i += 1
        k += 1
    inp[size - 1] = temp
    return inp


def check(inp):
    reverse = inp[::-1]
    if reverse == inp:
        return True
    return False


def checkPalindrome(inp):
    size = len(inp)
    op = inp

    for i in xrange(size):
        op = rotate(op)
        if check(op) == True:
            return True
    return False


if __name__ == '__main__':
    string = 'hhhjh'
    print checkPalindrome(string)