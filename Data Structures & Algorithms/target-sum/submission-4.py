class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def btrack(index, remainder):
            if (index, remainder) in memo:
                return memo[(index, remainder)]
            if index == n:
                return 1 if remainder == target else 0
            
            memo[(index, remainder)] = btrack(index+1, remainder+nums[index]) + btrack(index+1, remainder-nums[index])
            return memo[(index, remainder)]

        return btrack(0, 0)