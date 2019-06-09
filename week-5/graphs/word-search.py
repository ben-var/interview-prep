class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return not word
        
        def dfs(coord, board, word, let_idx, visited):
            if coord in visited: return False
            h, w = len(board), len(board[0])
            i, j = coord
            
            if i >= h or j >= w or i < 0 or j < 0 or board[i][j] != word[let_idx]:
                return False
            elif let_idx == len(word)-1:
                return board[i][j] == word[let_idx]
            
            visited.add(coord)
                
            ret = dfs((i-1, j), board, word, let_idx+1, visited) or \
                    dfs((i+1, j), board, word, let_idx+1, visited) or \
                    dfs((i, j-1), board, word, let_idx+1, visited) or \
                    dfs((i, j+1), board, word, let_idx+1, visited)
                
            visited.remove(coord)
            return ret
        
        first, starts = word[0], []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first:
                    starts.append((i,j))
        
        if not starts: return False
        
        for coord in starts:
            if dfs(coord, board, word, 0, set()):
                return True
        return False