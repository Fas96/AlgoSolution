class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)-1
        for i in range(n):
            if i>n-i:break
            s[i],s[n-i]=s[n-i],s[i]
        