from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_indices = []
        c2 = Counter(p)
        c1 = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            # sliding window to satisfy runtime requirement
            # instead of reinitializing c2 every iteration
            c1[s[i]] += 1
            if c1 == c2:
                start_indices.append(i-len(p)+1)
                
            prev = s[i-len(p)+1]
            c1[prev] -= 1
            if c1[prev] <= 0:
                del c1[prev]
        return start_indices
                
        