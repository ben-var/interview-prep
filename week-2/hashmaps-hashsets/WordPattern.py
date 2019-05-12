class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(pattern) != len(words): return False
        
        mapping, used = {}, set()
        for i in range(len(pattern)):
            # if word not already mapped
            if mapping.get(pattern[i]) == None and words[i] not in used:
                mapping[pattern[i]] = words[i]
                used.add(words[i])
            elif mapping.get(pattern[i]) != words[i]:
                return False
        return True
        