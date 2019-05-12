class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        
        rows,cols = len(board), len(board[0])
        
        if rows != cols or rows != 9:
            return False
    
        subgrid_sets = [[],[],[]]
        for i in range(3):
            for j in range(3):
                subgrid_sets[i].append(set())       
                    
        row_sets, col_sets = {}, {}
        for i in range(rows):
            row_sets[i], col_sets[i] = set(), set()
            
        for i in range(rows):
            for j in range(cols):
                x = board[i][j]
                if x == ".":
                    continue
                
                # check valid num and sudoku rule
                x = int(x)
                if x < 1 or x > 9 or x in row_sets[i] or x in col_sets[j]:
                    return False
                
                # find the correct subgrid coordinate, and check subgrid rule
                grid_i, grid_j = i // 3, j // 3
                if x in subgrid_sets[grid_i][grid_j]:
                    return False
                
                # add number to relevant sets
                row_sets[i].add(x)
                col_sets[j].add(x)
                subgrid_sets[grid_i][grid_j].add(x)
        
        # if no rule violations, board is valid
        return True
                
        