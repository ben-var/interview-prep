class Solution:
    def titleToNumber(self, s: str) -> int:
        
        chars = list(s)
        base = 64
        col_num = 0
                
        pow = 0
        for i in range(1,len(chars)+1):
            col_num += (ord(chars[-i]) - base) * (26**pow)
            pow += 1
            
        return col_num