class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, n in  enumerate(nums):
            diff = target - n
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[n] = i