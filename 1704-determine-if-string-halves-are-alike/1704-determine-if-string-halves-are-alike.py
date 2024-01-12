class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vs = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n1, n2 = 0, 0
        for i in range(len(s)//2):
            if s[i] in vs: n1+=1
            if s[-i-1] in vs: n2+=1
        return n1==n2
        