class Solution:
    def longestPalindrome(self, s: str) -> int:
        f=Counter(s)
        ans=0
        odd=[]
        t=False
        for k,v in f.items():
            ans= ans+v if v%2==0 else ans+(v-1)
            if v%2==1: t=True
                
        return ans+1 if t else ans