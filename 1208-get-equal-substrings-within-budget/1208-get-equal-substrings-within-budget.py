class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans,cost,L=0,0,0
         
        for idx in range(n):
            cost+=abs(ord(s[idx])-ord(t[idx]))
            while cost>maxCost:
                cost-=abs(ord(s[L])-ord(t[L]))
                L+=1
            ans=max(ans,idx-L+1)
        return ans