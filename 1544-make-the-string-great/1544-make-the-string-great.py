class Solution:
    def makeGood(self, s: str) -> str:
        n=len(s)
        stk=[]
        for i in range(len(s)):
            if stk and abs(ord(stk[-1])-ord(s[i]))==32:
                stk.pop()
            else:
                stk.append(s[i])
        return "".join(stk)
                
            