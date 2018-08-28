def power(n,i):
    if i == 0:
        return 1.0
    else:
        if i < 0:
            return power(1.0/n,i*-1)
        else:
            return (n * power(n, i - 1))

if __name__ == '__main__':
    print power(2,-2)