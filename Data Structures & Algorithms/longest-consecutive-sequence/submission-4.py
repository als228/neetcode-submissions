class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set()
        
        for n in nums:
            s.add(n)
        for n in nums:
            if n-1 not in s:
                seq = 1
                while n+1 in s:
                    seq += 1
                    n += 1
                res = max(res, seq)
        
        return res