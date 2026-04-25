class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False for _ in range(len(nums))]

        def dfs(l, vis):
            for i in range(0, len(nums)):
                v = vis[:]
                if not v[i]:
                    l.append(nums[i])
                    v[i] = True
                else:
                    continue
                
                if len(l) == len(nums):
                    res.append(l[:])
                else:
                    dfs(l[:], v)
                l.pop()
        
        dfs([], visited)
        return res