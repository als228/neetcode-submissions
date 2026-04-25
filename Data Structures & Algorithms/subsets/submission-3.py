class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def btrack(num_list, index):
            res.append(list(num_list))
            for j in range(1, len(nums)-index):
                copy = list(num_list)
                copy.append(nums[index+j])
                btrack(copy, index+j)
        
        for i in range(len(nums)):
            btrack([nums[i]], i)
        
        return res