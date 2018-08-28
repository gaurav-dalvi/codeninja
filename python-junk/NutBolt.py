def NutBoltMatch(nutArr, boltArr, low, high):
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        partition (bolts, low, high, nuts[pivot])

        NutBoltMatch(nuts,bolts,low,pivot-1)
        NutBoltMatch(nuts, bolts, pivot + 1, high)

def partitio(arr, low, high, pivot):


if __name__ == '__main__':
    nutArr = ['N3', 'N2', 'N1', 'N5', 'N4']
    boltArr = ['B1', 'B2', 'B5', 'B3', 'N4']
    NutBoltMatch(nutArr, boltArr, 0, 5)