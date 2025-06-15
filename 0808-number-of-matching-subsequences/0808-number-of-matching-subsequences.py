class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int: 
        def subseq(st):
            pos = -1
            for char in st:
                pos = s.find(char, pos+1)
                if pos == -1: return False
            return True
        return sum(map(subseq, words))