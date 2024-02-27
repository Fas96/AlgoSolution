class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(':')', '{':'}','[':']'}
        stk = []
        for i in s:
            if i in mp:
                stk.append(i)
            elif len(stk) == 0 or mp[stk.pop()] != i:
                return False
        return len(stk) == 0
                    
        