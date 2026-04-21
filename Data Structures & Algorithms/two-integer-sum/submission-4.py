class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i in range(len(nums)):
            dictNums[nums[i]] = i
            
        for i in range(len(nums)):
            diff = target - nums[i]
            if (dictNums.get(diff) is not None and dictNums.get(diff) != i):
                return [i, dictNums.get(diff)]
