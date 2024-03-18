from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    maxi = 0
    # Write your code here
    for i in range(len(nums)):
        l = len(nums[i:])
        sumy = sum(nums[i:])

        if sumy == k and l > maxi:
            return l
            l
        else:
            for j in range(len(nums)-1, i, -1):
                if sumy - nums[j] == k:
                    l -= 1
                    maxi = max(maxi, l)
                else:
                    sumy -= nums[j]
                    l -= 1
    
    return maxi
    pass
