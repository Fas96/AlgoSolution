class Solution(object):
    def makeEqual(self, words):
        
        return all(val % len(words) == 0 for val in collections.Counter(''.join(words)).values())