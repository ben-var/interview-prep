class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, best_buy = 0, float("Inf")
        if len(prices) < 2: return profit
                
        for p in prices:
            if p < best_buy:
                best_buy = p
            profit = max(p - best_buy, profit)
        
        return profit