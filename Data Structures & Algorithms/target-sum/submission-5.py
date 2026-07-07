class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0:1}

        for num in nums:
            nxt = defaultdict(int)
            
            for val, count in dp.items():
                nxt[val+num] += count
                nxt[val-num] += count

            dp = nxt
        
        return dp[target]