class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False for _ in range(len(nums))]

        def dfs(l, vis):
            for i in range(0, len(nums)):
                if vis[i]:
                    continue
                else:
                    l.append(nums[i])
                    vis[i] = True
                    
                    if len(l) == len(nums):
                        res.append(l[:])
                    else:
                        dfs(l, vis)
                    l.pop()
                    vis[i] = False
        
        dfs([], visited)
        return res