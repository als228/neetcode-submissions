class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dictNums:
                return [dictNums[diff], i]
            dictNums[n] = i
