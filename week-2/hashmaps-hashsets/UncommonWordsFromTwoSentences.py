class Solution:
    def mapWords(self, word_map, words):
        for w in words:
            if word_map.get(w) == None:
                word_map[w] = 1
            else:
                word_map[w] += 1
        return word_map
    
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_count_map = {}
        words_A, words_B = A.split(" "), B.split(" ")
        
        word_count_map = self.mapWords(word_count_map, words_A)
        word_count_map = self.mapWords(word_count_map, words_B)
        
        unique_words = []
        for k, v in word_count_map.items():
            if v == 1:
                unique_words.append(k)
        return unique_words

        
        