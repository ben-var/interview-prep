class UnionFind(object):
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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # general idea is to connect all edge "O" to a dummy node
        # then connect each O to a neighboring O if any, such that
        # eventually the connection to the edge is stored and
        # can be updated in the final loop
        
        if not board: 
            return
        
        h,w = len(board), len(board[0])
        is_O = w*h
        
        uf = UnionFind(is_O+1)
        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    # if on border
                    if i==0 or j==0 or i==h-1 or j==w-1:
                        uf.union(is_O, i*w + j)
                    else:
                        for (di, dj) in [[1,0], [0,1], [-1,0], [0,-1]]:
                            new_i, new_j = i+di, j+dj
                            
                            if new_i < 0 or new_j < 0 or new_i > h-1 or new_j > w-1:
                                continue
                            elif board[new_i][new_j] == "O":
                                uf.union(i*w+j, new_i*w+new_j)
                        

        
        for i in range(1,h-1):
            for j in range(1,w-1):
                if board[i][j] == "O" and uf.find(i*w + j) != uf.find(is_O):
                    board[i][j] = "X"