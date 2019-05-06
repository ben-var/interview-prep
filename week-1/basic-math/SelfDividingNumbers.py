class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for n in range(left, right+1):
            if n % 10 == 0:
                continue
            
            num = n
            self_dividing = num > 0
            while num > 0:
                if num % 10 == 0 or n % (num % 10) != 0:
                    self_dividing = False
                    break
                
                num = num // 10
            
            if self_dividing:
                arr.append(n)
                
        return arr