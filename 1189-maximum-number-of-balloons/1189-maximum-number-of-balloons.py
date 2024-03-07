class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=Counter('balloon')
        t=Counter(text)
        ans=float('inf')
        for c in b: 
            ans=min(ans,t[c]//b[c])
            
        return ans if ans!=float('inf') else 0
            
        