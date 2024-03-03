class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        x=True
        res=""
        for i in range(0,len(s),k):
            
            if x:
                res+=(s[i:i+k][::-1])
                x=False
            else:
                x=True
                res+=s[i:i+k]
                
        return res
            
        