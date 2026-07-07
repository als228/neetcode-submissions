class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # initialize dp table
        n = len(nums)
        target = sum(nums) // 2
        memo = {}
        
        def dfs(index, remainder):
            if remainder == 0:
                return True
            if remainder < 0 or index >= n:
                return False
            if (index, remainder) in memo:
                return memo[(index, remainder)]
            
            memo[(index, remainder)] = dfs(index+1, remainder-nums[index]) or dfs(index+1, remainder)
            return memo[(index, remainder)]
        
        return dfs(0, target)