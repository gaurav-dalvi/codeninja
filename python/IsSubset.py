# Return true if Set1 is subset of set2
# otherwise return False

def isSubset(set1, set2):
    if set1 is None or set2 is None:
        # null set is subset of any other set
        return True

    size1 = len(set1)
    size2 = len(set2)

    if size1 == 0:
        # empty set is subset of any other set
        return True

    if size1 > size2:
        return False

    index = 0
    flag = False
    for i in xrange(size2):
        if index == size1:
            return True
        elif set1[index] < set2[i]:
            return False
        elif set1[index] > set2[i]:
            continue
        elif set1[index] == set2[i]:
            flag = True
            index = index + 1

    if flag == False:
        return False

    if index == size1:
        return True

    return False


if __name__ == '__main__':
    # Assuming sets are sroted
    set1 = [4, 6, 7, 9]
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = [4, 6, 7, 9]
    set2 = [4, 6, 7, 9]
    print isSubset(set1, set2)

    set1 = [4, 6]
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = [7, 9]
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = [1, 2]
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = []
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = None
    set2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print isSubset(set1, set2)

    set1 = [1, 9, 10]
    set2 = []
    print isSubset(set1, set2)

    set1 = [1, 9, 10]
    set2 = None
    print isSubset(set1, set2)

    set1 = [1, 9, 10]
    set2 = [1, 7, 8, 11]
    print isSubset(set1, set2)
