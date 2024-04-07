class Solution:
    def checkValidString(self, s: str) -> bool:
        op=cl=st=0 
        for c in s:
            op+=(c=='(')
            cl+=(c==')')
            st+=(c=='*') 
            if cl>op+st:return False
        op=cl=st=0
        for c in s[::-1]:
            op+=(c=='(')
            cl+=(c==')')
            st+=(c=='*') 
            if op>cl+st:return False
        return True
        