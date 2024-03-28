class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sf=Counter(t)
        for x in s:
            if x in sf:
                sf[x]-=1
            else:
                sf[x]=1
       
        for x in t:
            if sf[x]>0: return x
        return ""
        