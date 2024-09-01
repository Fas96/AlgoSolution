class Solution:
    def checkTwoChessboards(self, c: str, c1: str) -> bool:
        df={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        return ((df[c[0]]+int(c[1]))%2)==((df[c1[0]]+int(c1[1]))%2)
        