class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Recurrence: P[i] = max(0, prices[i] - prices[i-1] + P[i-1])
        # prices[i] - prices[i-1] is profit/loss per day, P[i-1] is profit from before
        # if total profit becomes negative, buying at that day is preferable.
        
        if not prices: return 0
        
        P = [0] * len(prices)
        for i in range(1, len(prices)):
            P[i] = max(0, prices[i]-prices[i-1]+ P[i-1])
        return max(P)