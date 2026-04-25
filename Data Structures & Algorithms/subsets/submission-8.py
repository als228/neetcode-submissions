class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def btrack(num_list, index):
            for j in range(index, len(nums)):
                num_list.append(nums[j])
                res.append(list(num_list))
                btrack(num_list, j+1)
                num_list.pop()
        
        btrack([], 0)
        return res