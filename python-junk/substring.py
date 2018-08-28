class Name():

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

def solution():

    arr = []
    counter = 100
    for i in xrange(1,10):
        n = Name(i,counter)
        counter = counter - 10
        arr.append(n)

    arr.sort(key=lambda x: x.val2)
    for i in xrange(len(arr)):
        print arr[i].val1,
        print arr[i].val2

def comparator(a,b):
    if a.val2 > b.val2:
        return 1
    elif a.val2 == b.val2:
        return 0
    else:
        return -1

if __name__ == '__main__':
    # sizeN = int(raw_input())
    # inp = raw_input()
    # arr = [int(i) for i in inp.split()]
    # if len(arr) != 3:
    #     print 'Invalid input'
    # else:
    #     K = arr[0]
    #     L = arr[1]
    #     M = arr[2]
    #
    # strInp = raw_input()
    #
    # print sizeN , K, L , M , strInp
    solution()
