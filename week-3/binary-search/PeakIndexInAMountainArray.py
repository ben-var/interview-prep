class Solution:
    def binary_search(self, A, left, right):
        mid = (right+left) // 2
        
        # constant time comparison O(1)
        if right - left <= 2:
            if A[right] > A[left] and A[right] > A[mid]:
                return right
            elif A[left] > A[right] and A[left] > A[mid]:
                return left
            else:
                return mid
            
        
        if right == left:
            return right
        
        # logarithmic time reduction of problem
        if A[mid+1] < A[mid] and A[mid-1] < A[mid]:
            return mid
        elif A[mid+1] >= A[mid]: # go right
            return self.binary_search(A, mid+1, right)
        else:
            return self.binary_search(A, left, mid-1)
        
        
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.binary_search(A, 0, len(A)-1)
        