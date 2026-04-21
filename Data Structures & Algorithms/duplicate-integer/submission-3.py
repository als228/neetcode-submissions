class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = 1
            else:
                return True
        return False 