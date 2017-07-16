# Input : 1?0?
# Output: 1000, 1001, 1100, 1101

def wildChar(input, index):
    if index == len(input):
        print input
        return
    else:
        if input[index] == '?':
            input[index] = '0'
            wildChar(input,index + 1)
            input[index] = '1'
            wildChar(input,index + 1)
            input[index] = '?'
        else:
            wildChar(input,index + 1)
    
if __name__ == '__main__':
    input = raw_input("")
    li = list(input)
    wildChar(li, 0)
