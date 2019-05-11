class UnionFind(object):
    def __init__(self, N):
        self.data = [i for i in range (N)]
    
    def find(self, i):
        if self.data[i] == i:
            return i
        return self.find(self.data[i])
    
    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)
        self.data[j_parent] = i_parent

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # could also have used DFS here. when a 1 is encountered, increment numIslands
        # counter and then flip all connected 1s to 0, including the first one encountered.
        
        if not grid:
            return 0
        
        w = len(grid[0])
        h = len(grid)
        
        uf = UnionFind(w*h)
        for i in range(h):
            for j in range(w):
                for (dx, dy) in [[1,0], [0, 1]]:
                    adj_i = i + dy
                    adj_j = j + dx
                    if adj_i < 0 or adj_j < 0 or adj_i > h-1 or adj_j > w-1:
                        continue
                    elif grid[i][j] == "1" and grid[adj_i][adj_j] == "1":
                        uf.union(i*w + j, adj_i*w + adj_j)
        s = set()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    s.add(uf.find(i*w+j))
        return len(s)