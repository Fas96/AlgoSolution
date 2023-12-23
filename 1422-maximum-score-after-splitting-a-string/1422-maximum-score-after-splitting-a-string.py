class Solution:
    def maxScore(self, s: str) -> int:
        
        n=len(s)
        ans=0
        for i in range(1,n): 
            ans=max(ans,s[:i].count('0')+s[i:].count('1'))
        return ans
        