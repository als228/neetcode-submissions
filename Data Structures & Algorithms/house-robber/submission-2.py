class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        ans = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if i-3 >= 0:
                nums[i] += max(nums[i-2], nums[i-3])
            else:
                nums[i] += nums[i-2]
            ans = max(ans, nums[i])
        
        return ans