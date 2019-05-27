class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        
        # idea is to expand 'lowest' until an interval is reached
        # that does not intersect with lowest. Sorted by first element
        # of each interval. 
        intervals.sort()
        merged = []
        lowest = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] <= lowest[1]:
                lowest[1] = max(lowest[1], interval[1])
                
                if i == len(intervals) - 1:
                    merged.append(lowest)
            else:
                merged.append(lowest)
                lowest = interval
                
                if i == len(intervals) - 1:
                    merged.append(interval)
        return merged
    
    def partitionLabels(self, S: str) -> List[int]:
        charset = set(list(S))
        intervals = []
        for c in charset:
            start = S.find(c)
            end = S.rfind(c)
            if end == -1:
                end = len(S) - 1
            intervals.append([start,end])
        
        merged = self.merge(intervals)
        res = []
        for interval in merged:
            res.append(interval[1] - interval[0] + 1)
            
        return res