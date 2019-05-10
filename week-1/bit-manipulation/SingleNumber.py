class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleton = 0
        for n in nums:
            singleton ^= n
        return singleton