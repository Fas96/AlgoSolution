class Trie: 
    def __init__(self): 
        self.r = [None] * 26
        self.isEnd = False
        

    def insert(self, word: str) -> None: 
        node = self
        for c in word:
            i = ord(c) - ord('a')
            if not node.r[i]:
                node.r[i] = Trie()
            node = node.r[i]
        node.isEnd = True
        

    def search(self, word: str) -> bool: 
        node = self
        for c in word:
            i = ord(c) - ord('a')
            if not node.r[i]:
                return False
            node = node.r[i]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool: 
        node = self
        for c in prefix:
            i = ord(c) - ord('a')
            if not node.r[i]:
                return False
            node = node.r[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)