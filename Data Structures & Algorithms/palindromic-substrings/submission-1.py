class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # for odd
        for i, c in enumerate(s):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        # for even
        for i, c in enumerate(s):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res