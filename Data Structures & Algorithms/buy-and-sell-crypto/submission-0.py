class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_gap = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                gap = prices[sell] - prices[buy]
                max_gap = max(max_gap, gap)
            else:
                buy = sell
            sell += 1

        return max_gap