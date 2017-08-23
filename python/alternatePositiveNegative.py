# Give an array containing positive and negative number, arrange them in a such way that there is alternative +ve and -ve  and it should be stable.
#
# Input = 2 3 -4 -9 -1 -7 1 -5 -6
# Output = 2 -4 3 -9 1 -1 -7 -5 -6
#
# Can you implement without using any extra space.

# using extra constant space , O(n) time complexity
# http://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
# - O(1) space and O(N2) time

# http://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/
# http://www.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/

def arrange_alternate(numbers):

    for i in xrange(len(numbers)): # why do u need this line
        j = 0
        while j + 2 < len(numbers):
            s = [numbers[j], numbers[j+1], numbers[j+2]]
            s = [1 if x >= 0 else -1 for x in s]
            if s[0] == s[1] and s[1] != s[2]:
                numbers[j+1], numbers[j+2] = numbers[j+2], numbers[j+1]
            j += 1

def rotate_array(numbers, out_of_place, cur):

    # rotate array to right between out_of_place and cur index
    temp = numbers[cur]
    for i in xrange(cur, out_of_place, -1):
        numbers[i] = numbers[i-1]

    numbers[out_of_place] = temp

def arrange_alternate_1(numbers):

    out_of_place = -1

    for i in xrange(len(numbers)):
        if out_of_place >= 0:
            if (numbers[i] >= 0 and numbers[out_of_place] < 0) or (numbers[i] < 0 and numbers[out_of_place] >= 0):
                rotate_array(numbers, out_of_place, i)
                # the new out of place entry is two steps ahead
                if i - out_of_place > 2:
                    out_of_place = out_of_place + 2
                else:
                    out_of_place = -1

        if out_of_place == -1:
            if (numbers[i] >= 0 and (i & 0x01) == 0) or (numbers[i] < 0 and (i & 0x01) == 1):
                out_of_place = i


if __name__ == '__main__':
    a = [2,3,-4,-9,-1,-7,1,-5,-6]
    arrange_alternate_1(a)
    print a

    a = [-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]
    arrange_alternate_1(a)
    print a

    a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    arrange_alternate_1(a)
    print a

    a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    arrange_alternate_1(a)
    print a
