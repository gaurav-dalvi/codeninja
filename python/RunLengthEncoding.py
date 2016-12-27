def RunLengthEncoding(string):
    size = len(string)
    count = 0
    i = 0
    temp = ''
    while i < size:
        rLen = 1
        while (i+1 < size and string[i] == string[i+1]):
            rLen += 1
            i += 1

        if rLen != 1:
            temp = temp + str(rLen) + string[i]
        else:
            temp = temp + string[i]
        i += 1

    if len(temp) >= len(string):
        return string
    return temp

if __name__ == '__main__':
    print RunLengthEncoding('AAABB')
