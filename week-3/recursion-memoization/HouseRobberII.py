class Solution:
    def robOne(self, i, nums, memo):
        if i >= len(nums):
            return 0
        elif i in memo:
            return memo[i]
        profit = max(nums[i] + self.robOne(i+2, nums, memo), self.robOne(i+1, nums, memo))
        memo[i] = profit
        return profit
    
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        
        first = nums[:-1]
        second = nums[1:]
        return max(self.robOne(0, first, {}), self.robOne(0, second, {}))