class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()
    
    def charToIndex(self, c):
        return ord(c) - ord('a')
    
    def insert(self, key):
        ptr = self.root
        for level in range(len(key)):
            c = self.charToIndex(key[level])
            if not ptr.children[c]:
                ptr.children[c] = self.getNode()
            ptr = ptr.children[c]
        ptr.isEndOfWord = True
    
    def search(self, key): 
        ptr = self.root
        for level in range(len(key)):
            c = self.charToIndex(key[level])
            if not ptr.children[c]:
                return False
            ptr = ptr.children[c]
        return ptr != None and ptr.isEndOfWord
                
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # set solution accomplishes the same thing and is actually more efficient,
        # but this exercise is to learn to use a basic implementation of a trie
	# the trie could also have a special function that returns the result 
	# desired for this function.

        t = Trie()
        for w in words:
            t.insert(w)
            
        longest, longestWord = -1, chr(ord('z') + 1)
        for w in words:
            if len(w) >= longest:
                
                # check if word is lexicalgraphically before current longest word
                if len(w) == longest and w > longestWord:
                    continue
                
                isBuilt = True
                for i in range(len(w)):
                    # search each subword
                    if not t.search(w[:i+1]):
                        isBuilt = False
                        break
                    
                if isBuilt:
                    longest, longestWord = len(w), w
        return longestWord