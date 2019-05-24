class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        return sum(nums[1::2])