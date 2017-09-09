# We are given large array 4 byte integers. We need to write method to find out how many total bits are
# turned on (set it to 1)
#
# eg:
# arr = [31,51] ans = 9 as 31 has 5 bits and 51 has 4 bits turned on
# arr = [2147483647, 3] ans = 31 + 2 = 33
#
# Give fast solution. Dont worry about machine architecture. Assume base 10 input no floating points
# https://en.wikipedia.org/wiki/Hamming_weight

def generate_count_bits():

    # To generate bit count for all integers between 0 to 65536 (2^16) -> 2 bytes
    count_bits = [0] * 65536
    for i in xrange(65536):
        x = i
        count = 0
        while x > 0:
            x = x & (x-1)
            count = count + 1
        count_bits[i] = count

    return count_bits


def hamming_weights(arr):

    count_bits = generate_count_bits()
    count = 0
    for item in arr:
        count = count + count_bits[item & 0xFFFF] + count_bits[item >> 16]
    return count


if __name__ == '__main__':
    arr = [31,51]
    print hamming_weights(arr)

    arr = [2147483647,3]
    print hamming_weights(arr)
