class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
                
        # binary operation could be done here, but this will quickly
        # converge to a solution because multiple crosses n exponentially fast
        for i in range(n):
            multiple = 2**i
            
            if multiple > n:
                return False
            if multiple == n:
                return True

        return False