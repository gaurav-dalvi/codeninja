# Problem : https://www.ideserve.co.in/learn/maximum-size-square-sub-matrix-with-all-1s
# Key Points to remember:
# 1: How to declare 2D array in pytuon - create col_length of lists and create those many row_length lists
# 2: How to find min from 3 numbers, minimu if else cases

def min_number(i, j, k):
    first_min = min(i, j)
    final_min = min(first_min, k)
    return final_min


def max_square_matrix(matrix):
    if matrix is None:
        raise Exception("Invalid Input")
    row_length = len(matrix)
    col_length = len(matrix[0])

    max_sq_size = 0
    filter_matrix = [[0 for x in range(col_length)] for y in range(row_length)]
    for i in xrange(row_length):
        for j in xrange(col_length):
            if i == 0 or j == 0:
                filter_matrix[i][j] = matrix[i][j]
            elif matrix[i][j] == 0:
                filter_matrix[i][j] = 0
            else:
                filter_matrix[i][j] = min_number(filter_matrix[i - 1][j - 1], filter_matrix[i - 1][j], filter_matrix[i][j - 1]) + 1
                if filter_matrix[i][j] > max_sq_size:
                    max_sq_size = filter_matrix[i][j]

    return filter_matrix, max_sq_size


if __name__ == '__main__':
    matrix = [[1, 1, 0, 0, 1, 1],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 1, 1]]

    print max_square_matrix(matrix)
