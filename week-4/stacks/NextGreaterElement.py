class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map indices to speed up search time
        indices = {}
        for i, n in enumerate(nums2):
            indices[n] = i
        
        res = []
        for n in nums1:
            start = indices[n]
            
            # find the next greatest integer, if any
            for i in range(start, len(nums2)+1):
                if i == len(nums2):
                    res.append(-1)
                elif nums2[i] > n:
                    res.append(nums2[i])
                    break
        return res