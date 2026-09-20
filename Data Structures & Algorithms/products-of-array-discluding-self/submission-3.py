class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            postfix[len(nums)-1-i] = nums[len(nums)-i] * postfix[len(nums)-i]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        
        return res