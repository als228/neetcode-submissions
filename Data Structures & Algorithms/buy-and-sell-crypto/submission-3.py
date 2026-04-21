class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0

        for r in range(len(prices)):
            res = max(res, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r
        
        return res