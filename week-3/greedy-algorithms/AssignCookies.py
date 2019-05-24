from collections import Counter

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        # originally had slow n^2 algorithm. in fact, if sorted,
        # each child has to be satisfied in order, and cookies that
        # cannot satisfy less greedy children can be ignored for 
        # greedier children, thus the count can be made in one pass
        # 
        # sorting dominates the complexity of O(nlogn)
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
            
        return child
                