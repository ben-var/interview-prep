class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
         "..",".---","-.-",".-..","--","-.","---",".--.",
         "--.-",".-.","...","-","..-","...-",".--","-..-",
         "-.--","--.."]
        morse_map = {}
        
        char_int = ord('a')
        for m in morse:
            morse_map[chr(char_int)] = m
            char_int += 1
        
        transformations = set()
        for w in words:
            transformation = ""
            for char in w:
                transformation += morse_map[char]
            transformations.add(transformation)
            
        return len(transformations)
                
            