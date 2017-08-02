# Group given array as even and odd
# Do it in one pas of array. In place grouping.
# input array is positive integers only

def groupNumbers(intArr):
    left = 0
    right = len(intArr) - 1

    while left < right:
        while (intArr[left] % 2) == 0 and left < right:
            left = left + 1
        while (intArr[right] % 2) == 1 and left < right:
            right = right - 1
        if left < right:
            intArr[left], intArr[right] = intArr[right], intArr[left]
            left = left + 1
            right = right - 1

    return intArr

if __name__ == '__main__':

    inpList = [3,7,10,12,24,15,9,8]
    print groupNumbers(inpList)
