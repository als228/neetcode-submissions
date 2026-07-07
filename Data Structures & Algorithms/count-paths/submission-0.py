class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a dp table
        dp = [[0]*n for _ in range(m)]
        
        # only one path for row 0
        for i in range(n):
            dp[0][i] = 1
        # only one path for col 0
        for i in range(m):
            dp[i][0] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]