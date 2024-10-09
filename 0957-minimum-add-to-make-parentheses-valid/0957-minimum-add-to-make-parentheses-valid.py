class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans,b=0,0
        for c in s:
            if c=='(':
                b+=1
            elif b:
                b-=1
            else: ans+=1
        return ans+b
        