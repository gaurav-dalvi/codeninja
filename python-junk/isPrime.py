import math

def checkPrime(number):

    if number == 2 or number == 3:
        return True

    # To handle negative numbers
    if number < 0:
        number = number * (-1)

    target = int(math.sqrt(number)) + 1

    for i in xrange(2, target):
        if number % i == 0:
             return False

    return True

if __name__ == '__main__':
    string = raw_input()
    try:
        number = int(string)
        print checkPrime(number)
    except ValueError:
        print 'Invalid input'