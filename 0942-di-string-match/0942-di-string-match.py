class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm=[]
        L,R=0,len(s)
        
        
        for c in s:
            if c=='I':
                perm.append(L)
                L+=1
            elif c=='D':
                perm.append(R)
                R-=1
        perm.append(L)
        return perm
        