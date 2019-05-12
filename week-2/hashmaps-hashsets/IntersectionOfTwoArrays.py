class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A, B = set(nums1), set(nums2)
        return list(A.intersection(B))