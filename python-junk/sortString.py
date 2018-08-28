def sortString(inp):

    inputList = list(inp)
    # Declaring 2D array
    col = 256
    row = 2
    asciiMap = [0] * 256
    for i in xrange(len(inputList)):
        count = asciiMap[ord(inputList[i])]
        asciiMap[ord(inputList[i])] = count + 1

    # storing input in array
    index = 0
    for i in xrange(256):
        if asciiMap[i] > 0:
            for j in xrange(asciiMap[i]):
                inputList[index] = chr(i)
                index = index + 1

    return ''.join(inputList)

if __name__ == '__main__':
    print sortString('AAAABAAAA')