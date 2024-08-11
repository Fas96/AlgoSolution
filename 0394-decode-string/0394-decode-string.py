class Solution:
    def decodeString(self, s: str) -> str:
        ans=[]
        for c in s:
            if c!=']':
                ans.append(c)
            else:
                st=""
                while  ans[-1]!='[':
                    st=ans.pop()+st
                ans.pop()
                n=""
                while ans and ans[-1].isdigit():
                    n=ans.pop()+n
                st=int(n)*st
                ans.append(st)             
        return "".join(ans)
        