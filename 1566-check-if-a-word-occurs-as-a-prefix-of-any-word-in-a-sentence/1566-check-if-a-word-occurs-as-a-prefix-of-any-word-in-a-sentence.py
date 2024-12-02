class Solution:
    def isPrefixOfWord(self, sentence: str, sw: str) -> int:
        idx=1 
        for x in sentence.split(" "): 
            if x.startswith(sw):
                return idx
            idx+=1
        return -1
        