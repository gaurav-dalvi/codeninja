def solution(inp, data, index):
    if index == len(inp):
        print data
    else:
        for i in xrange(len(inp)):
            data[index] = inp[i]
            solution(inp, data, index+1)


if __name__ == '__main__':
    A = ['A', 'B', 'C']
    data = ['', '', '']
    solution(A, data, 0)
    
# ['A', 'A', 'A']
# ['A', 'A', 'B']
# ['A', 'A', 'C']

# ['A', 'B', 'A']
# ['A', 'B', 'B']
# ['A', 'B', 'C']

# ['A', 'C', 'A']
# ['A', 'C', 'B']
# ['A', 'C', 'C']

# ['B', 'A', 'A']
# ['B', 'A', 'B']
# ['B', 'A', 'C']

# ['B', 'B', 'A']
# ['B', 'B', 'B']
# ['B', 'B', 'C']

# ['B', 'C', 'A']
# ['B', 'C', 'B']
# ['B', 'C', 'C']

# ['C', 'A', 'A']
# ['C', 'A', 'B']
# ['C', 'A', 'C']

# ['C', 'B', 'A']
# ['C', 'B', 'B']
# ['C', 'B', 'C']

# ['C', 'C', 'A']
# ['C', 'C', 'B']
# ['C', 'C', 'C']
