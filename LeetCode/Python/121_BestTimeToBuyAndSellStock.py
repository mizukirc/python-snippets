class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
s = Solution()
prices = [7,1,5,3,6,4]
