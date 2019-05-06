class Solution:
    def isPalindrome(self, s: str) -> bool:
        # format string
        s = s.lower()
        s = s.translate(s.maketrans('','', string.punctuation))
        s = s.replace(" ", "")
        
        # iterative to save memory space and save time on formatting
        while len(s) > 2:
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                return False

        
        if len(s) <= 1:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False