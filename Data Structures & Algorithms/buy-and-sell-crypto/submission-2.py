class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        f, l = 0, 0

        for i, p in enumerate(prices):
            if p < prices[f]:
                f, l = i, i
            if p > prices[l]:
                l = i
            
            profit = max(profit, prices[l] - prices[f])
        
        return profit