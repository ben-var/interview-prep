from bisect import insort

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        start_indices = []
        window_size = len(p)
        window = sorted(s[:window_size])
        
        for i in range(window_size-1, len(s)):
            if i >= window_size:
                window.remove(s[i-window_size])
                insort(window, s[i])
            if p == window:
                start_indices.append(i-window_size+1)
        return start_indices