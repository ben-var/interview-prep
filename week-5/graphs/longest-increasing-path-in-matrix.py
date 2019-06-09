# unoptimized (fails ~3/147 testcases due to timeout)
# DP required for optimization

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        h, w = len(matrix), len(matrix[0])
        
        def dfs(pos, visited, prev):
            i, j = pos
            if i >= h or j >= w or i < 0 or j < 0 or matrix[i][j] <= prev:
                return 0
            
            curr = matrix[i][j]
                        
            visited.add((i,j))
            longest = 1 + max(dfs((i+1, j), visited, curr),
                             dfs((i-1, j), visited, curr),
                             dfs((i, j+1), visited, curr),
                             dfs((i, j-1), visited, curr))
            return longest
    
        longest = float('-Inf')
        for i in range(h):
            for j in range(w):
                longest = max(longest, dfs((i,j), set(), float('-Inf')))
        return longest