class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, rem_target, num_list):
            for i in range(index, len(nums)):
                t = rem_target - nums[i]
                if t > 0:
                    copy = num_list + [nums[i]]
                    dfs(i, t, copy)
                elif t == 0:
                    copy = num_list + [nums[i]]
                    res.append(copy)
        
        dfs(0, target, [])
        
        return res