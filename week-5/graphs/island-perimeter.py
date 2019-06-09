class Solution:
    def countLines(self, grid, i, j, h, w):
        neighbors = [[0,1], [1,0], [0,-1], [-1,0]]
        
        lines = 0
        for di, dj in neighbors:
            new_i, new_j = i + di, j + dj
        
            if new_i >= h or new_j >= w or new_i < 0 or new_j < 0 or grid[new_i][new_j] == 0:
                lines += 1
        return lines
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        
        num_lines = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    num_lines += self.countLines(grid, i, j, h, w)
        return num_lines