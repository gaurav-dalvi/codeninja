# Given a set of n nuts of different sizes and n bolts of different sizes.
# There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.
# Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed.
# It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
#
# Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one key in the box.
# We need to match the pair.


def MatchPairs(nuts, bolts, first, last):
    if first < last:
        index = Partition(nuts, first, last, bolts[last])
        Partition(bolts, first, last, nuts[index])

        MatchPairs(nuts, bolts, first, index -1)
        MatchPairs(nuts, bolts, index + 1, last)

def Partition(arr, start, end, pivot):

    index = start
    j = start
    while j < end:
        if arr[j] < pivot:
            # swap arr[index] and arr[j]
            arr[j], arr[index] = arr[j], arr[index]
            index = index + 1
        elif arr[j] == pivot:
            # swap arr[j] and arr[end]
            arr[j], arr[end] = arr[end], arr[j]
            j = j - 1
        j = j + 1

    # Swap arr[index] and arr[end]
    arr[end], arr[index] = arr[index], arr[end]

    return index

if __name__ == '__main__':
    nuts = ['@', '#', '$', '%', '&']
    bolts = ['$', '%', '&', '@', '#']

    MatchPairs(nuts, bolts, 0, len(nuts) - 1)

    print nuts
    print bolts
