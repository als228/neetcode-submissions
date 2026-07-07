class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def btrack(index, remainder):
            if index == n and remainder == target:
                return 1
            if index == n and remainder != target:
                return 0
            
            return btrack(index+1, remainder+nums[index])+btrack(index+1, remainder-nums[index])
        
        return btrack(0, 0)