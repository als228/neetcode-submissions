class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            if sell < minBuy:
                minBuy = sell
            if maxProfit < sell - minBuy:
                maxProfit = sell - minBuy
        return maxProfit