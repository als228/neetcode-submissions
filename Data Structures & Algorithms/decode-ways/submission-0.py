class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0

        for i in range(len(s)-2, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i+1]
            
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        
        return dp[0]