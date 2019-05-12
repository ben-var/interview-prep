class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create an isomorphic mapping from s -> t and vice-versa
        # if inconsistency is found, return False, otherwise Truep        
        map_s, map_t = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if map_s.get(c1) == None:
                map_s[c1] = c2
            if map_t.get(c2) == None:
                map_t[c2] = c1
            
            if map_s[c1] != c2 or map_t[c2] != c1:
                return False
        return True