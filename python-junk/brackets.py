def Driver(n):
    if n > 0:
        Brackets(0,n,0,0)
    return
def Brackets(pos, n , open, close):
    op = []
    if close == n:
        print ''.join(op)
        return
    else:
        if open > close:
            op[pos] = ')'
            Brackets(pos+1, n, open, close+1)
        if open < n:
            op[pos] = '('
            Brackets(pos + 1, n, open+1, close)
if __name__ == '__main__':
    Driver(3)