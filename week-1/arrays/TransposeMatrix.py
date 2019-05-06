class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        # would like to revisit to make more efficient. 
        # new to python complexity :)
        num_rows = len(A[0])
        
        transpose = []
        for i in range(num_rows):
            transpose.append([])
            
        for row in A:
            for j in range(num_rows):
                transpose[j].append(row[j])
        
        return transpose