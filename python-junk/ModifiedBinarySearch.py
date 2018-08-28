# Given an array of sorted integers which is rotated any number of times,
# find minimum element from the array

def ModifiedBinarySearch(nums, low, high):

    mid = (high + low) / 2
    if low == high:
        return nums[low]
    else:
        if nums[mid] > nums[high]:
            return ModifiedBinarySearch(nums, mid+1, high)
        else:
            return ModifiedBinarySearch(nums, low, mid)

if __name__ == '__main__':
    nums = [5,2,3]
    print ModifiedBinarySearch(nums, 0, len(nums)-1)