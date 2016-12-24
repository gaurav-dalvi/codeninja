# Check if a String is a palindrome, using Recursion. Ignore punctuation, normal
# whitespace characters and case.
# Punctuation characters are (c == '.' || c == ',' || c == '!' || c == '-' || c == ';' || c
# == ':' || c== '\'' || c == '"'). Feel free to use an IDE or Google for language
# constructs if you don't know.
#
# Input
# A paragraph of input. Could be just a single line, or could be just a character. Can
# have line breaks
#
# Output
# Boolean, whether it's a palindrome or not, ignoring above punctuation.
# e.g.
# racecar ==> yes
# Never a foot too far, even. => yes
# test => no
# a => yes

def isPalindrome(string):

    punctuation = ['.', ',', '!', '-', ';', ':', '\\', '"', ' ', '\n']
    tempString = ''

    for i in string:
        if i not in punctuation:
            tempString += i

    length = len(tempString)
    end = length / 2
    tempString = tempString.lower()
    print tempString
    print length, end

    for i in xrange(end):
        if tempString[i] != tempString[(length-1) - i]:
            return False
        elif i > (length-1) - i:
            return True
    return True

if __name__ == '__main__':
    print isPalindrome('ever a foot t fareve')
