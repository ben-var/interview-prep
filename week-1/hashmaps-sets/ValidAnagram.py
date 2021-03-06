class Solution:
    
    # returns a map for each character of a string to its total number of occurences 
    def fillCharMap(self, s):
        chars = {}
        for i in range(len(s)):
            
            if chars.get(s[i]) == None:
                chars[s[i]] = 1
            else:
                chars[s[i]] += 1
        return chars
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = self.fillCharMap(s)
        
        for i in range(len(t)):
            if s_chars.get(t[i]) == None or s_chars[t[i]] <= 0:
                return False
            else:
                s_chars[t[i]] -= 1
        return True
