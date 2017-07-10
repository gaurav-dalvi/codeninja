def seqPrint(low, high):
    print low,
    if low < high:
        seqPrint(low+1, high)
        print low,

if __name__ == '__main__':
    seqPrint(3,7)