class Solution:
    def longestPalindrome(self, s: str) -> int:
        f=Counter(s)
        ans=0
        odd=[]
        t=False
        for k,v in f.items():
            if v%2==0:
                ans+=v
            else:
                t=True
                ans+=(v-1)
                
 
        return ans+1 if t else ans
            