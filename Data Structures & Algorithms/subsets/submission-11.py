class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def backtrack(subset, index):
            for i in range(index, len(nums)):
                subset.append(nums[i])
                ans.append(list(subset))
                backtrack(subset, i+1)
                subset.pop()
        
        backtrack([], 0)
        return ans