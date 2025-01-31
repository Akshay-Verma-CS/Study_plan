class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0
        while p1 <= len(prices) - 1 and p2 < len(prices):
            if prices[p1] >= prices[p2]:
                p1 = p2
                p2+=1
            elif prices[p1] < prices[p2]:
                diff = prices[p2] - prices[p1]
                if diff > profit:
                    profit = diff
                p2+=1
        return profit
