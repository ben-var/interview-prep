def minDistance(self, word1: str, word2: str) -> int:
        
        if not word1 or not word2:
            return max(len(word1), len(word2))
        
        n, m = len(word1)+1, len(word2)+1
        T = [[0] * m for _ in range(n)] # n x m dimension
        
        for i in range(n):
            T[i][0] = i
        for j in range(m):
            T[0][j] = j
            
        for i in range(1, n):
            for j in range(1, m):
                if word1[i-1] == word2[j-1]: # if letter is same
                    T[i][j] = T[i-1][j-1]
                else: 
                    T[i][j] = 1 + min(T[i][j-1], T[i-1][j], T[i-1][j-1])
        
        return T[-1][-1]