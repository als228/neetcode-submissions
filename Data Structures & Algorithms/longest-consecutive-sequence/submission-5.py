class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in nums:
            if n-1 not in s:
                seq = 1
                while n+1 in s:
                    n += 1
                    seq += 1
                res = max(res, seq)
        
        return res