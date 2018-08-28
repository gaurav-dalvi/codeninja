# Search in a row wise and column wise sorted matrix
# Given an n x n matrix, where every row and column is sorted in increasing order.
# Given a number x, how to decide whether this x is in the matrix.
# The designed algorithm should have linear time complexity.

def searchSortedMatrix(matrix, key, row, cols):

    rowIndex = 0
    colIndex = cols - 1

    while rowIndex < row and colIndex >= 0:
        if matrix[rowIndex][colIndex] == key:
            return True
        else:
            if matrix[rowIndex][colIndex] < key:
                rowIndex += 1
            else:
                colIndex -= 1
    return False

if __name__ == '__main__':

    matrix = [[10, 20, 30, 40],
              [11, 22, 37, 42],
              [13, 25, 39, 50]]

    print searchSortedMatrix(matrix, 70, 3, 4)