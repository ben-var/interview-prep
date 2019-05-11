class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            sum_squared = 0
            while (n > 0):
                sum_squared += (n % 10)**2
                n //= 10
            
            if sum_squared in visited:
                return False
            
            n = sum_squared
            visited.add(n)
        else:
            return True
            
