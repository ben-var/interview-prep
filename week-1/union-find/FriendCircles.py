class UnionFind:
    def __init__(self, N):
        self.data = [i for i in range(N)]
    
    def find(self, i):
        if self.data[i] == i:
            return i
        return self.find(self.data[i])

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)
        self.data[j_parent] = i_parent
        
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # identical to num_islands problem
        # except in this case there's only N students
        # so unionfind is over N elements of N x N matrix
        if not M:
            return 0
        
        h,w = len(M), len(M[0])
        
        uf = UnionFind(h)
        
        for i in range(h):
            for j in range(w):
                if M[i][j] == 1:
                    uf.union(i, j)
        
        s = set()
        for i in range(h):
            for j in range(w):
                if M[i][j] == 1:
                    s.add(uf.find(i))
                    
        return len(s)