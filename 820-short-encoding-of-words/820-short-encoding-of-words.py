class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []

    def insert(self, word): #None
        root = self.root
        for symbol in word:
            root = root.children[symbol]
        self.ends.append((root, len(word) + 1))

        
class Solution:
    def minimumLengthEncoding(self, words):
        trie, ans = Trie(), 0
        
        for word in set(words):
            trie.insert(word[::-1])
        
        return sum(depth for node, depth in trie.ends if len(node.children) == 0)