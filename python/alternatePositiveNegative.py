# Give an array containing positive and negative number, arrage them in a such way that there is alternative +ve and -ve  and it should be stable.
#
# Input = 2 3 -4 -9 -1 -7 1 -5 -6
# Output = 2 -4 3 -9 1 -1 -7 -5 -6
#
# Can you implement without using any extra space.


def arrageAlternate(numbers):

    for i in xrange(len(numbers)):
        j = 0
        while j + 2 < len(numbers):
            s = [numbers[j], numbers[j+1], numbers[j+2]]
            s = [1 if x >= 0 else -1 for x in s]
            if s[0] == s[1] and s[1] != s[2]:
                numbers[j+1], numbers[j+2] = numbers[j+2], numbers[j+1]
            j += 1


if __name__ == '__main__':
    a = [2,3,-4,-9,-1,-7,1,-5,-6]
    arrageAlternate(a)
    print a
