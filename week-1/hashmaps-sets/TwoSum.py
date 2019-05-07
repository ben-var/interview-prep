class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            n = nums[i]
            # target - n is value that would complete the two sum solution
            # duplicate indices are also checked in the condition
            if (target - n) in map.keys() and i != map[target-n]:
                return [i, map[target-n]]
        
        return None