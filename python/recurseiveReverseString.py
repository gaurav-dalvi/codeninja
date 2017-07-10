def Reverse(inp):
    print inp
    if inp == '':
        return inp
    else:
        return inp[-1] + Reverse(inp[:-1])

if __name__ == '__main__':
    s = 'GAURAV'
    op = Reverse(s)
    print op