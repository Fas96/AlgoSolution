class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sf,tf={},{}
        for x,y in zip(s,t):
            if (x in sf and sf[x]!=y) or ( y in tf and tf[y]!=x):
                return False
            sf[x]=y
            tf[y]=x
            
            
        return True
        