class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        ones = self.climbStairs(n-1)
        twos = self.climbStairs(n-2)
        return ones+twos