
def get_chars(digit):

    phone_dict = {0:'',
                  1:'',
                  2:'ABC',
                  3:'def',
                  4:'ghi',
                  5:'jkl',
                  6:'mno',
                  7:'pqrs',
                  8:'tuv',
                  9:'wxyz'}
    if digit < 0 or digit > 9:
        return ''
    return phone_dict[digit]

def solution(input):

if __name__ == "__main__":

    solution()
