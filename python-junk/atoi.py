# Convert a string to an integer.
#
# atoi() first discards as many whitespace characters as necessary until the first non-whitespace
# character is found. Then, starting from this character, it takes an optional plus or minus sign,
# followed by as many numerical digits as possible and interprets them as numerical value.
# The string can contain additional characters after those that form the integral numbers, which
# are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no
# such sequence exists because either str is empty, or it contains only whitespace characters,
# then no conversion is performed.
# If no valid conversion is performed, a zero value is returned.
#
# e.g.
# "-3924x8fc" = -3924
# "c++" = 0
# "++1" = 0

def  atoiIK(str):
    realStr = str.lstrip()
    plusMinus = ['+','-']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    isNegative = False
    if realStr[0] == '-':
        isNegative = True
        realStr = realStr[1:]
    value = 0

    for i in xrange(len(realStr)):
        if realStr[i] in digits:
            value = (value *10) + (ord(realStr[i]) - ord('0'))
        else:
            if value > 0:
                 break
            else:
                return 0

    if isNegative is True:
        value = value * -1
    return value

if __name__ == '__main__':
    print atoiIK('-3924x8fc')
    print atoiIK('78')