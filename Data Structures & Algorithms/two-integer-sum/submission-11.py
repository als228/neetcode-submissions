class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            if n not in res: 
                res[n] = []
            res[n].append(i)
            diff = target - n
            if diff in res and i is not res[diff][0]:
                return [res[diff][0], i]