from typing import *

def reverse(arr, nums, n):
    if n == -1:
        return arr
    else:
        arr.append(nums[n])
        return reverse(arr, nums, n-1)

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    arr = []
    return reverse(arr, nums, n-1)
    pass
