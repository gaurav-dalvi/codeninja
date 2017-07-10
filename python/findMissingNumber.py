# You are given N distinct positive numbers from 1 through N. But one of them is missing. i.e.
# you're really only given N-1 numbers. How will you find that missing number?
# We want a solution that is linear time and constant space.
# Input: An array of N-1 positive integers, in no particular order. There are NO repeated
# numbers. Each number occurs only once. Assume valid input.
# Output: The missing number
# e.g.
#
# Input: 4,1,2,6,5
# Output: 3
#
# In the above example, N = 6. You're given an array of 5 numbers from 1 thru 6, with number 3 missing.

def findMissingNumber(intArr):
    totalSum = 0
    for i in xrange(len(intArr)):
        totalSum = totalSum + intArr[i]
    n = len(intArr) + 1
    realSum = (n * (n + 1)) / 2
    return (realSum - totalSum)

if __name__ == '__main__':
    print findMissingNumber([4,1,2,5,6])