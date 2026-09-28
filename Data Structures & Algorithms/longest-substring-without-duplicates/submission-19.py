class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0
        l = 0

        for r, char in enumerate(s):
            if char in chars:
                while l < r and s[l] != char:
                    chars.remove(s[l])
                    l += 1
                l += 1
            else:
                chars.add(char)
                res = max(res, r-l+1)
        
        return res