class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        fa,fb=Counter(word1),Counter(word2)
        for k,v in fa.items():
            if  abs(v-fb[k])>3:return False 
        for k,v in fb.items():
            if abs(v-fa[k])>3:return False 
        return True
        