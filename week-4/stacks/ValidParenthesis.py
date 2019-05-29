class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'{':'}','(':')','[':']'}
        lefts = set(mapping.keys())
        
        stack = []
        for c in s:
            if c in lefts:
                stack.append(c)
            elif not stack:
                return False
            else:
                check = stack.pop(-1)
                if mapping[check] != c:
                    return False
                
        return not stack 