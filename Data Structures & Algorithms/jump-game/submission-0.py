class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0

        for i, num in enumerate(nums):
            if current >= i:
                current = max(current, i+num)
            else:
                return False
        
        return True