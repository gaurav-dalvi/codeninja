

def converTime(time):
    flag = 'AM'
    if 'AM' == time[-2:]:
        flag = 'AM'
    else:
        flag = 'PM'

    if flag == 'PM':
        if time[:2] == '12':
            ans = time[:-2]
        else:
            time_slice = str((int(time[:2]) + 12) % 24)
            ans = time_slice + time[2:-2]

    else:  # AM Case
        if time[:2] == '12':
            ans = '00' + time[2:-2]
        else:
            ans = time[:-2]

    print ans

if __name__ == '__main__':
    converTime('01:45:54PM')

