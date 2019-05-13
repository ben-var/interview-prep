from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        val = c.most_common(1)[0][0]
        max_num = max(nums)
        
        for i in range(1,max_num+2):
            if c[i] == 0:
                return [val, i]