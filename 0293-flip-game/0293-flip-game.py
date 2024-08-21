class Solution:
    def generatePossibleNextMoves(self, c: str) -> List[str]:
        an=[]
        n=len(c)
        for i in range(n-1):
            if c[i]=="+" and c[i+1]=="+":
                an.append(c[:i]+"--"+c[i+2:])
        return an