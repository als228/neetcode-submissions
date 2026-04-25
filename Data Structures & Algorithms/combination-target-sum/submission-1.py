class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, rem_target, num_list):
            for i in range(index, len(nums)):
                t = rem_target - nums[i]
                if t < 0:
                    continue
                num_list.append(nums[i])
                if t == 0:
                    res.append(num_list[:])
                else:
                    dfs(i, t, num_list)
                num_list.pop()
        
        dfs(0, target, [])
        
        return res