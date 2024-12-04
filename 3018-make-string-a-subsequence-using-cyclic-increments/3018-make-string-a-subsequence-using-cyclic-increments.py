class Solution:
    def canMakeSubsequence(self, so: str, s: str) -> bool:
        id,l=0,len(s)
        for x in so:
            if id<l and (ord(s[id])-ord(x))%26<2:
                id+=1
        return id==l
        