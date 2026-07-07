class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.helper(nums[:len(nums)-1]), 
            self.helper(nums[1:])
        )
    
    def helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        res = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if i - 3 >= 0:
                nums[i] += max(nums[i-2], nums[i-3])
            else:
                nums[i] += nums[i-2]
            res = max(res, nums[i])
        
        return res