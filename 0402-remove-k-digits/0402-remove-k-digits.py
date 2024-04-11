class Solution:
    def removeKdigits(self, num: str, k: int) -> str: 
        if k==len(num):return "0"
        rem=len(num)-k
        stk=[]
        for c in num:
            while k and stk and stk[-1]>c:
                stk.pop()
                k-=1
            stk.append(c)
        return ''.join(stk[:rem]).lstrip('0') or '0'
        
            
                    
        