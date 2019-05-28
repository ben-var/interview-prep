class Solution: 
    def isMatch(self, s: str, p: str) -> bool:
        # sol from https://leetcode.com/problems/regular-expression-matching/solution/
        n, m = len(s) + 1, len(p) + 1
        T = [[False] * m for _ in range(n)]
        
        T[-1][-1] = True
            
        for i in range(n-1, -1, -1):
            for j in range(m-2, -1, -1):
                match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j+1 < len(p) and p[j+1] == '*':
                    T[i][j] = T[i][j+2] or match and T[i+1][j]
                else:
                    T[i][j] = match and T[i+1][j+1]
                    
        return T[0][0]