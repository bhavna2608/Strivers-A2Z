def search(nums: [int], target: int):
    # write your code logic !!'
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        else:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
