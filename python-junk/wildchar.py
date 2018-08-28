def wildChar(input, index):
    if index == len(input):
        print input
        return
    if input[index] == '?':
        input[index] = '0'
        wildChar(input, index + 1)
        input[index] = '1'
        wildChar(input, index + 1)
        input[index] = '?'
    else:
        wildChar(input,index + 1)

if __name__ == '__main__':
    inp = '1?1?'
    l = list(inp)
    #print l, len(l)
    wildChar(l,0)