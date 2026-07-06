class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = (0, "")

        for l in range(len(s)):
            for r in range(len(s)-1, l-1, -1):
                if isPalindrome(l, r, s):
                    if (r-l+1) > res[0]:
                        res = r-l+1, s[l:r+1]
                    break
        
        return res[1]