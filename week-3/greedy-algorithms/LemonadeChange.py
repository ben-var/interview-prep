class Solution:
    def giveChange(self, order, fives, tens):
        if order == 5: 
            fives += 1
        elif order == 10:
            fives -= 1
            tens += 1
        else:
            # want the biggest bills gone first if possible
            if not tens:
                fives -= 3
            else:
                tens -= 1
                fives -= 1
            
        return fives, tens
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for b in bills:            
            fives, tens = self.giveChange(b, fives, tens)
            
            if fives < 0 or tens < 0:
                return False
        return True
                