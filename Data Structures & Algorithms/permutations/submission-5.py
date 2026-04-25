class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False for _ in range(len(nums))]

        def dfs(l):
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                else:
                    l.append(nums[i])
                    visited[i] = True
                    
                    if len(l) == len(nums):
                        res.append(l[:])
                    else:
                        dfs(l)
                    l.pop()
                    visited[i] = False
        
        dfs([])
        return res