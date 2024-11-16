class Solution:
    def isCircularSentence(self, s: str) -> bool:
        ans=True
        n=len(s.split(" "))
        s=s.split(" ")
        for i in range(n-1): 
            if i+1<n and s[i][-1]!=s[i+1][0]:
                ans=False
        return s[0][0]==s[len(s)-1][-1] and ( ans)
        