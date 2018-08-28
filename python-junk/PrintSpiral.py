RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def print_spiral_driver(n):
    matrix = [[0 for x in xrange(5)] for y in xrange(5)]
    print_spiral(1, 2,2, matrix, n, RIGHT)
    print_matrix(matrix,5,5)

def print_matrix(matrix, row, col):

    for i in xrange(row):
        for j in xrange(col):
            print matrix[i][j],
        print '\n'

def print_spiral(count, row, col, matrix, n, direction):
    if count == n:
        return
    else:
        for i in xrange(count):
            if direction == RIGHT:
                matrix[row][col] = '*'
                col = col + 1
            elif direction == DOWN:
                matrix[row][col] = '*'
                row = row + 1
            elif direction == LEFT:
                matrix[row][col] = '*'
                col = col - 1
            elif direction == UP:
                matrix[row][col] = '*'
                row = row - 1
            else:
                print 'ERROR'
                return
        print_spiral(count + 1, row, col, matrix, n, (direction + 1)%4)


if __name__ == '__main__':
    print_spiral_driver(25)
