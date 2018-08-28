import sys


def StairCase(n):
    if n > sys.maxint:
        print 'Integer size is not allowed'
        return

    space = ' '
    spaceCount = n - 1
    for i in xrange(n):
        print space * spaceCount, '#' * (i + 1)
        spaceCount = spaceCount - 1

if __name__ == '__main__':
    StairCase(6)