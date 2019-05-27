class Solution:
    def edit(self, word1, word2, i, j, memo):
        
        if i >= len(word1) and j >= len(word2):
            return 0
        elif i >= len(word1):
            return len(word2) - j
        elif j >= len(word2):
            return len(word1) - i
        
        if (i,j) not in memo:
            if word1[i] == word2[j]:
                memo[(i,j)] = self.edit(word1, word2, i+1, j+1, memo)
            else:
                insert = 1 + self.edit(word1, word2, i+1, j, memo)
                delete = 1 + self.edit(word1, word2, i, j+1, memo)
                replace = 1 + self.edit(word1, word2, i+1, j+1, memo)
                
                memo[(i,j)] = min(insert,delete,replace)
        return memo[(i,j)]
              
    def minDistance(self, word1: str, word2: str) -> int:
        return self.edit(word1, word2, 0, 0, {})