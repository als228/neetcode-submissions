class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        # 1st pass
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        
        # 2nd pass
        for i in range(k, len(nums)):
            if q[0] <= i-k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res