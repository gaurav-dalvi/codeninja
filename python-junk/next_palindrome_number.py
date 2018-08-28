# Given a number, find the next smallest palindrome
# Given a number, find the next smallest palindrome larger than this number. For example,
# if the input number is 2 3 5 4 5, the output should be 2 3 6 3 2. And if the input number is 9 9 9, the output should be 1 0 0 1.
#
# The input is assumed to be an array. Every entry in array represents a digit in input number. Let the array be num[] and size of array be n
#
# There can be three different types of inputs that need to be handled separately.
# 1) The input number is palindrome and has all 9s. For example 9 9 9. Output should be 1 0 0 1
# 2) The input number is not palindrome. For example 1 2 3 4. Output should be 1 3 3 1
# 3) The input number is palindrome and doesnt have all 9s. For example 1 2 2 1. Output should be 1 3 3 1.

 #http://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/


def next_palindrome_number(number):


if __name__ == '__main__':
    print next_palindrome_number(99)
    print next_palindrome_number(8998)
    print next_palindrome_number(6789876)
    print next_palindrome_number(23545)
    print next_palindrome_number(23701)