class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l, r = 0, 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                maxL = max(r - l, maxL)
            else:
                seen.remove(s[l])
                l += 1
        
        return maxL