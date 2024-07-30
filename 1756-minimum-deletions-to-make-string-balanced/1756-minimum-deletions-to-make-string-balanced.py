class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans,b=0,0
      
        for v in s:
            if v=='a':
                ans=min(ans+1,b)
            else:
                b+=1
             
        return ans