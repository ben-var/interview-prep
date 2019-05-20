class Solution:
    # recursive function to perform the search
    def binary_search(self, nums: List[int], target: int, minimum: int, maximum: int) -> int:
        # base cases
        if minimum > maximum:
            return -1
       
        pivot = (maximum+minimum) // 2
        
        if nums[pivot] == target: # found
            return pivot
        elif nums[pivot] > target: # go left
            return self.binary_search(nums, target, minimum, pivot-1)
        else: # go right
            return self.binary_search(nums, target, pivot+1, maximum)
   
    # helper function to kickoff the binary search
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)