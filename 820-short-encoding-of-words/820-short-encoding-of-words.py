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
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict()) 
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)
