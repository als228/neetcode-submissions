class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        maxLen = max(len(word) for word in wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True

        for r in range(1, len(s)+1):
            for l in range(max(0, r-maxLen), r):
                if dp[l] and s[l:r] in words:
                    dp[r] = True
                    break

        return dp[-1]