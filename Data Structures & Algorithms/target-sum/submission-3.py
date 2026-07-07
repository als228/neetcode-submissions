class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def btrack(index, remainder):
            if (index, remainder) in memo:
                return memo[(index, remainder)]
            if index == n and remainder == target:
                return 1
            if index == n and remainder != target:
                return 0
            
            memo[(index+1, remainder+nums[index])] = btrack(index+1, remainder+nums[index])
            memo[(index+1, remainder-nums[index])] = btrack(index+1, remainder-nums[index])
            return memo[(index+1, remainder+nums[index])] + memo[(index+1, remainder-nums[index])]
        
        return btrack(0, 0)