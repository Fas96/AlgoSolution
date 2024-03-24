class Solution:
    def countHousePlacements(self, n: int) -> int:
        f,s=0,1
        for i in range(n+1): f,s=s,f+s
        return (s*s)%((10**9)+7) 
        