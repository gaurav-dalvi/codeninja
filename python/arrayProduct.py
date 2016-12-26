# Given array of numbers, return an array of numbers `products` is the product of all
# the numbers nums[j], j!= i
#
# Input : [1,2,3,4,5]
# Output : [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
#          [120,60,40,30,24]
#
# You must do in O(N) time and constant space, without using division. Usage of
# intermediate product array in not considered extra space.
# http://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div

def arrayProducts(numbers):
    size = len(numbers)
    product_below = [0] * size
    product_above = [0] * size
    solution = [0] * size

    p = 1

    for i in xrange(size):
        product_below[i] = p
        p = p * numbers[i]

    p = 1
    for i in xrange(size-1,-1,-1):
        product_above[i] = p
        p = p * numbers[i]

    print product_below
    print product_above

    # Calculating Solution

    for i in xrange(size):
        solution[i] = product_below[i] * product_above[i]

    return solution

if __name__ == '__main__':
    print arrayProducts([1,2,3,4,5])
