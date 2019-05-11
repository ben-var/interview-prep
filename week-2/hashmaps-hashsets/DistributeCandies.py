class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candies = set(candies)
        return min(len(unique_candies), len(candies) // 2)
        
        