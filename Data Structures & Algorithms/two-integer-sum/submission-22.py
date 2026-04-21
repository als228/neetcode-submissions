class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        my_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                result.append(my_dict[diff])
                result.append(i)
            my_dict[nums[i]] = i
        return result