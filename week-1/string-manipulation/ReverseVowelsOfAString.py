class Solution:
    def reverseVowels(self, s: str) -> str:
        # not efficient - would like to understand the python string manipulations and complexity
        chars = list(s)
        reversed_vowels = list(copy.deepcopy(chars))
        
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        vowels.add('A')
        vowels.add('E')
        vowels.add('I')
        vowels.add('O')
        vowels.add('U')
        
        left = 0
        right = len(chars) - 1
        while left < right:
            while chars[left] not in vowels and left < right:
                left += 1
            while chars[right] not in vowels and right > 0:
                right -= 1
                
            if left > right: break
                
            reversed_vowels[left] = chars[right]
            reversed_vowels[right] = chars[left]
            left += 1
            right -= 1
                
        return "".join(reversed_vowels)