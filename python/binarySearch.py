# Implement Binary search.
# Key Learnings : mid -1 and mid+1 in recursive call

def binary_search_recursive(nums, low, high, key):

    mid = (high + low) / 2
    if nums[mid] == key:
        return True
    if low < high:
        if nums[mid] > key:
            return binary_search_recursive(nums, low, mid-1, key)
        else:
            return binary_search_recursive(nums, mid+1, high, key)
    return False

def binary_search_iterative(nums, low, high, key):

    while low <= high:
        mid = (low + high) / 2
        if nums[mid] == key:
            return True
        else:
            if nums[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

    return False


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    print binary_search_iterative(nums, 0, len(nums)-1, 8)
