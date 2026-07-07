class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True

        for r in range(1, len(s)+1):
            for l in range(0, r):
                if s[l:r] in words and dp[l]:
                    dp[r] = True

        return dp[-1]