class Solution:
    def maxDepth(self, s: str) -> int:
        stk=[]
        mx=float('-inf')
        for x in s:
            if x=="(":
                stk.append("(")
            elif x==")":
                mx=max(len(stk),mx)
                stk.pop()
        return mx if mx!=float('-inf') else 0
        