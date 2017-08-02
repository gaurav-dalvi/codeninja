# Find triplets from the given array whose sum is zero.
# This problem CAN NOT be done better than O(n2).
# http://www.programcreek.com/2012/12/leetcode-3sum/
#
# Related Problems:
# http://www.geeksforgeeks.org/find-number-of-triangles-possible/
# Sum exactly to given number
# Sum to nearest number to given integer K (Sort and do binary search to nearest)

def ThreeSumProblem(inp):
    size = len(inp)
    inp.sort()
    result = []

    for i in xrange(size - 2):
        if i == 0 or inp[i] > inp[i-1]:
            j = i + 1
            k = size - 1
            while j < k:
                if (inp[i] + inp[j] + inp[k]) == 0:
                    result.append([inp[i] ,inp[j] ,inp[k]])

                    j = j + 1
                    k = k - 1
                    # for fuplicates
                    while j < k and inp[j] == inp[j-1]:
                        j = j + 1
                    while j < k and inp[k] == inp[k+1]:
                        k = k - 1

                elif (inp[i] + inp[j] + inp[k]) < 0:
                    j = j + 1
                else:
                    k = k -1

    return result

if __name__ == '__main__':
    # result = ThreeSumProblem([-5,2,3,4,1,-4,0,3,2,6])
    # result = ThreeSumProblem([6,10,3,-4,1,-6,9])
    result = ThreeSumProblem([-1,0,1,2,-1,-4])
    for r in result:
        print str(r)
