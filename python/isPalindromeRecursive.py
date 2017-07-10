def isPalindromeRecursive(string):
    if string == '' or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return isPalindromeRecursive(string[1:len(string) - 1])

    return False


if __name__ == '__main__':
    print isPalindromeRecursive('GGAAGG')