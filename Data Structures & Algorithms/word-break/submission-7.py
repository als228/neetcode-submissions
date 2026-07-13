class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for r in range(n+1):
            for l in range(r):
                if dp[l] and s[l:r] in words:
                    dp[r] = True
                    break
        
        return dp[-1]