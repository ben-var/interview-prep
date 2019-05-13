from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # could also utilize difference of counters
        c1, c2 = Counter(s), Counter(t)
        for c in t:
            if c1[c] != c2[c]: return c