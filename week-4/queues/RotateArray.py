class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # suboptimal solution to ensure use of a queue.
        while len(nums) < k:
            k -= len(nums)
            
        for i in range(len(nums) - k):
            nums.append(nums.pop(0))