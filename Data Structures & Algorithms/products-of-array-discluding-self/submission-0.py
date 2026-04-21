class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []

        for num in nums:
            val = num * (prefix[-1] if prefix else 1)
            prefix.append(val)
        # prefix = [1, 2, 8, 48]
        for i in range(len(nums)-1, -1, -1):
            val = nums[i] * (postfix[-1] if postfix else 1)
            postfix.append(val)
        # postfix = [6, 24, 48, 48]
        postfix.reverse()
        # postfix = [48, 48, 24, 6]
        for i in range(len(nums)):
            val = (prefix[i-1] if i-1 >= 0 else 1) * (postfix[i+1] if len(postfix) > i+1 else 1)
            res.append(val)
        
        return res