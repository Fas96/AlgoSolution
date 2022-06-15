class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        w1 = {chr(97 + i): 0 for i in range(0, 26)}
        w2 = {chr(97 + i): 0 for i in range(0, 26)}
 
        for i in word1:
            w1[i] += 1
        for i in word2:
            w2[i] += 1
        for i in w1:
            if abs(w1[i] - w2[i]) > 3:
                return False
        return True