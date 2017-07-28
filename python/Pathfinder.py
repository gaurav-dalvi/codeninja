# Problem Description
# You are given a list of numbers (list) and a starting position (pos).
# Your goal is to find a sequence of jumps from the starting position to the end of the list, ending at list.size(). A valid jump at any position must be between zero and the value at that position in the list, i.e. list.get(pos), inclusive. You must return a list of valid jumps in sequence that lead to the end of the list, or null if no such sequence exists.
#
# Examples
# For list = [ 1, 2, 0 ] and pos = 0, the only valid path from position 0 to position 3 is [ 1, 2 ]. This sequence represents two jumps, first from position 0 to position 1, then from position 1 to position 3.
# For list = [ 2, 3, 0, 2, 2 ] and pos = 0, possible valid paths are:
# [ 1, 3, 1 ] jump from position 0 to 1, then from 1 to 4, then from 4 to 5
# [ 1, 2, 1, 1 ] jump from position 0 to 1, then from 1 to 3, then from 3 to 4, then 4 to 5
# [ 1, 2, 2 ] jump from position 0 to 1, then from 1 to 3, then from 3 to 5
# For list = [ 2, 1, 0 ] and any pos, there is no valid result, so the return value should be null.

def PathFinder(inpList, pathList, outList, pos):
    if pos == len(inpList):
        newList = outList[:]
        pathList.append(newList)
        return
    elif pos > len(inpList):
        return
    elif inpList[pos] == 0:
        return
    else:
        for i in xrange(0,inpList[pos]+1):
            if i == 0:
                continue
            else:
                outList.append(i)
                PathFinder(inpList, pathList, outList, pos + i)
                outList.pop()

if __name__ == '__main__':
    inpList = [1,2,0]
    outList = []
    pathList = []
    PathFinder(inpList, pathList, outList, 0)
    print pathList
