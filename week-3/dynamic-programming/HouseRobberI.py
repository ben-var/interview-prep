class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) < 3: return max(nums)

        R = [0] * len(nums)
        R[0],R[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            R[i] = max(nums[i] + R[i-2], R[i-1])
        return R[-1]
