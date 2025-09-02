class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        curr_profit = 0

        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R
            elif prices[R] > prices[L]:
                curr_profit += prices[R] - prices[L]
                L = R
        
        return curr_profit
