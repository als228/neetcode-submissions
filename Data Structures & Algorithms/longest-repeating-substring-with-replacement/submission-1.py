class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ltrs = {}
        l, res = 0, 0
        
        maxF = 0
        for r in range(len(s)):
            ltrs[s[r]] = 1 + ltrs.get(s[r], 0)
            maxF = max(maxF, ltrs[s[r]])

            while r - l + 1 - maxF > k:
                ltrs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res