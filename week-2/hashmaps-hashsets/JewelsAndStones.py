class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set()
        for j in J:
            jewel_set.add(j)
        
        num_jewels = 0
        for s in S:
            if s in jewel_set:
                num_jewels += 1
                
        return num_jewels