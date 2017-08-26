def reverse_number(num):
    ans = 0
    if num is None or num == 0:
        return ans

    reminder = 0
    division = 0

    while num > 0:
        reminder = num % 10
        division = num / 10
        ans = (ans * 10) + reminder
        num = division

    return ans

def is_palindrome(num):
    new_num = reverse_number(num)
    if new_num == num:
        return True
    else:
        return False

if __name__ == '__main__':
    print reverse_number(12345)
    print is_palindrome(123321)
