class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0
        
        for n in nums:
            cur_sum = max(n, n+cur_sum)
            res = max(res, cur_sum)
        
        return res