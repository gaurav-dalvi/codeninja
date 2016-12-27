# Implement Binary search.
# Key Learnings : mid -1 and mid+1 in recursive call

def binarySearch(nums, low, high, key):

    mid = (high + low) / 2
    if nums[mid] == key:
        return True
    if low < high:
        if nums[mid] > key:
            return binarySearch(nums, low, mid-1, key)
        else:
            return binarySearch(nums, mid+1, high, key)
    return False


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    print binarySearch(nums, 0, len(nums)-1, 3)
