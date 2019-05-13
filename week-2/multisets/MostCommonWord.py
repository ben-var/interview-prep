from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        # final test case is very tricky, found this line in the discussions
        words = re.findall(r'\w+', paragraph)
        
        c = Counter(words)
        for s in banned:
            del c[s]
        return c.most_common(1)[0][0]