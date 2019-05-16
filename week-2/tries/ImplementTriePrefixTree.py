class Trie:
    # started with array based implementation, but speed improved by 
    # 30% using hashmap implementation, and code was more elegant
    
    class Node:
        def __init__(self):
            self.children = {}
            self.isEndOfWord = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for i in range(len(word)):
            c = word[i]
            if ptr.children.get(c) == None:
                ptr.children[c] = self.Node()
            ptr = ptr.children[c]
        ptr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for i in range(len(word)):
            c = word[i]
            if ptr.children.get(c) == None:
                return False
            ptr = ptr.children[c]
        return ptr != None and ptr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if ptr.children.get(c) == None:
                return False
            ptr = ptr.children[c]
        return ptr != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)