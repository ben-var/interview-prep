from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        s = ""
        for c,count in counter.most_common(len(counter)):
            s += c*count
        return s