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
                    if dfs(j+1, remainder-nums[j]):
                        return True
            
            return False
        
        return dfs(0, target)