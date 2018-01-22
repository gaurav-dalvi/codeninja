# https://www.ideserve.co.in/learn/print-matrix-diagonally#algorithmVisualization
# Key points to remember:
# 1: to understand what was the exact order of printing, had to watch video. Ask interviewer
# 2: these two loops are very tricky
# 3: understand to split this problem into two separate pair of for loops is the big idea here.


def print_matrix_digonally(matrix):

    if matrix is None:
        raise Exception("Invalid input")

    row_count = len(matrix)
    col_cont = len(matrix[0])

    # First half
    for i in xrange(row_count):
        row_index = i
        for j in xrange(i+1):
            print matrix[row_index][j],
            if row_index == 0:
                break
            else:
                row_index = row_index - 1
        print ""

    # second half
    for i in xrange(1,col_cont):
        col_index = i
        for j in xrange(row_count-1,-1,-1):
            print matrix[j][col_index],
            col_index = col_index + 1
            if col_index >= col_cont:
                break

        print ""


if __name__ == '__main__':

    # matrix = [[1,2,3,4,5],
    #           [6,7,8,9,10],
    #           [11,12,13,14,15],
    #           [16,17,18,19,20]
    #           ]

    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    print_matrix_digonally(matrix)
