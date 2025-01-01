class Solution:
    def maxScore(self, s: str) -> int:
        ans=float("-inf")
        for i in range(len(s)):
            bs=0
            if len(s[:i])>0 and len(s[i:])>0: 
                bs+=s[:i].count("0") 
                bs+=s[i:].count("1")
            ans=max(ans,bs)
        return ans
        