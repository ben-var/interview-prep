memo = {}
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if (s,p) in memo:
            return memo[(s,p)]
        
        if not s and not p:
            memo[(s,p)] = True
            return True
        
        if s and not p:
            memo[(s,p)] = False
            return False
        
        if len(p) > 1 and p[1] == '*':
            
            if len(p) > 3 and p[3] == "*":
                if p[0] == p[2]:
                    return self.isMatch(s, p[2:])
                if p[0] == '.':
                    return self.isMatch(s, '.' + p[3:])
            
            if not s:
                return self.isMatch(s, p[2:])
            elif s[0] == p[0]:
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            elif p[0] == '.':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p) or self.isMatch('', p[2:])
            
            return self.isMatch(s, p[2:])
        
        elif s and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            memo[(s,p)] = False
            return False