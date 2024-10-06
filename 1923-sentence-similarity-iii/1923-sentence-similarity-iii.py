class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1) < len(s2):  
            s1, s2 = s2, s1 
        w1 = s1.split(' ')
        w2 = s2.split(' ')
        i = j = 0
        while i < len(w2) and w1[i] == w2[i]: 
            i += 1
        while j < len(w2) and w1[~j] == w2[~j]:  
            j += 1
        return i > (len(w2) - 1 - j)