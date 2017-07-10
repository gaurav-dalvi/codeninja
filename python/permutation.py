def permutation(input, index):
    if index == len(input):
        print input
        return
    for i in xrange(index,len(input)):
        swap(input,i, index)
        permutation(input, index+1)
        swap(input, index, i)


def swap(input, i,j):
    input[j], input[i] = input[i], input[j]

if __name__ == '__main__':
    permutation([1,2,3],0)