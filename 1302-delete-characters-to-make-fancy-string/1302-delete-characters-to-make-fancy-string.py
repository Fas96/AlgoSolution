class Solution:
    def makeFancyString(self, s: str) -> str: 
        for c in set(s):
            while s.find(c*3) != -1: 
                s = s.replace(c*3, c*2)
        return s
        