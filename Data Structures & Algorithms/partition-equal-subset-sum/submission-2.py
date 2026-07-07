class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # initialize dp table
        n = len(nums)
        target = sum(nums) / 2
        
        def dfs(index, remainder):
            for j in range(index, n):
                if nums[j] == remainder:
                    return True
                elif nums[j] > remainder:
                    continue
                else:
                    return dfs(j+1, remainder-nums[j])
            
            return False
        
        for i in range(n):
            if dfs(i, target):
                return True
        
        return False