class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(),s.sort()
        M,N=len(g),len(s)
        cnt,idx,idj=0,0,0
        
        while idx<M and idj<N:
            if g[idx]<=s[idj]:
                idx+=1
                idj+=1
                cnt+=1
            elif g[idx]>=s[idj]:
                idj+=1
        return cnt
        