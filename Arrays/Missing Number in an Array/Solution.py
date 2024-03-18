class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumy = sum(nums)
        summ = int(n*(n+1)/2)
        return summ - sumy
