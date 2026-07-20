class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # find start point
        def find_max(start, end):
            cur_max = -1, -float('inf')
            for i in range(start, end):
                if nums[i] >= cur_max[1]:
                    cur_max = i, nums[i]
            return cur_max
        
        # basic vars
        cur_max = find_max(0, k)
        res = [cur_max[1]]
        l, r = 1, k
        n = len(nums)
        
        # sliding
        while r < n:
            if nums[r] >= cur_max[1]:
                res.append(nums[r])
                cur_max = r, nums[r]
            elif l <= cur_max[0]:
                res.append(cur_max[1])
            else:
                cur_max = find_max(l, r+1)
                res.append(cur_max[1])
            l += 1
            r += 1
        
        return res