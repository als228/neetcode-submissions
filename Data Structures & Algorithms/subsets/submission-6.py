class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def btrack(num_list, index):
            for j in range(len(nums)-index):
                num_list.append(nums[index+j])
                res.append(list(num_list))
                btrack(num_list, index+j+1)
                num_list.pop()
        
        btrack([], 0)
        return res