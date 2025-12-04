class Solution:
    def countCollisions(self, D: str) -> int:
        n=len(D)
        if n==1: return 0
        l, r=0, n-1
        while l<r and D[l]=='L':l+=1
        while l<r and D[r]=='R':r-=1
        if l>=r: return 0
        return sum(D[i]!='S' for i in range(l, r+1))       