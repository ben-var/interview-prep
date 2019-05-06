class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        reversed = ""
        for i in range(len(words)):
            reversed += str(words[i][::-1])
            if i < len(words)-1:
                reversed += " "
        return reversed