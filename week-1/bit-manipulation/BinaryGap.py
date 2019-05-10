class Solution:
    def binaryGap(self, N: int) -> int:
        '''
            O(n) solution, N is number of bits. 
             Would like to understand how log(n) runtime 
             is achieved. Solution suggests O(log n) but 
             seems to still be O(n).
             
             https://leetcode.com/problems/binary-gap/solution/
        ''' 
        bin_N = bin(N)[2:]
        
        longest = 0
        start = end = -1
        for i in range(len(bin_N)):
            if bin_N[i] == "1":
                if start < 0:
                    start = i
                else:
                    end = i
                    longest = max(end-start, longest)
                    start = i
                
        return longest
            
                
                