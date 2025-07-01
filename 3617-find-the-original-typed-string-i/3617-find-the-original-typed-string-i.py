class Solution:
    def possibleStringCount(self, word: str) -> int:
        freq=Counter(word)
        N=len(word)
        if len(freq)==1:return N
        for i in range(1, len(word)):
            if word[i]!=word[i-1]:
                N-=1
        return N
        