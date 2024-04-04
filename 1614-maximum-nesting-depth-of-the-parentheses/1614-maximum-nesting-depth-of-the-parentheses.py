class Solution:
    def maxDepth(self, s: str) -> int:
        dep=0
        mx=float('-inf')
        for x in s:
            if x=="(":
                dep+=1
            elif x==")":
                dep-=1
            mx=max(dep,mx) 
        return mx if mx!=float('-inf') else 0
        