class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        return self.helperClimbStairs(n, res)

    def helperClimbStairs(self, n: int, res: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        ones = self.helperClimbStairs(n-1, res)
        twos = self.helperClimbStairs(n-2, res)
        return ones+twos