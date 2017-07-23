# Input: 5
# Output:
# 
#      *
#    * * *
#  * * * * *
#    * * *
#      *

# prints number of spaces and stars in one line
def utilityPrint(arr, stars, spaces):
    temp = spaces / 2
    size = len(arr)
    i = 0
    while i <  size:
        while temp > 0:
            arr[i] = ' '
            i = i + 1
            temp = temp - 1
        temp = spaces / 2
        while stars > 0:
            arr[i] = '*'
            i = i + 1
            stars = stars - 1
        while temp > 0:
            arr[i] = ' '
            i = i + 1
            temp = temp - 1

    for i in xrange(size):
        print arr[i],
    print ' '

def printStar(size):

    for i in xrange((size/2) + 1):
        stars = (2*i) + 1
        spaces = size - stars
        arr = [0] * size
        utilityPrint(arr, stars, spaces)

    for i in xrange((size/2) + 1, size):
        stars = 2 * (size - i) - 1
        spaces = size - stars
        arr = [0] * size
        utilityPrint(arr, stars, spaces)


if __name__ == '__main__':
    printStar(11)
