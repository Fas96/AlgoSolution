class Solution:
    def makeGood(self, s: str) -> str:
        stk=[] 
        for x in s:
            stk.append(x)
            if len(stk)>1:
                if (stk[-1]!=stk[-2]) and (stk[-1]==stk[-2].lower() or stk[-1].lower()==stk[-2]):
                    stk.pop()
                    stk.pop()
        return ''.join(stk)
        