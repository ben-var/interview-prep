class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        points.sort(key = lambda x: x[1])
                       
        # originally was popping elements from the list when they
        # were able to be popped then moving x to the end of the leftover
        # balloon in the sorted list, but it was just fast enough to satisfy
        # the problem. This solution removes the popping and is much more
        # performant
        arrows = 0
        x = float('-Inf')
        for b in points:
            if b[0] > x:
                arrows += 1
                x = b[1]
            
        return arrows
        
        
                
