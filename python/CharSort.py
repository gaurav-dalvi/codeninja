# Sort array of chars, ASCII only.
# Input : String of chars , terminated by newline of NULL
# Output: Sorted set of chars. You can overwrite array.
# Desired complexity : O(n) with constant space

def sortCharacters(inString):
    inputList = list(inString)
    asciiMap = [0] * 256
    for i in xrange(len(inputList)):
        count = asciiMap[ord(inputList[i])]
        asciiMap[ord(inputList[i])] = count + 1
    
    # stroing input in array
    index = 0
    for i in xrange(256):
        if asciiMap[i] > 0:
            for j in xrange(asciiMap[i]):
                inputList[index] = chr(i)
                index = index + 1
    
    return ''.join(inputList)

if __name__ == '__main__':
    inString = 'afrslfirew'
    print sortCharacters(inString)
