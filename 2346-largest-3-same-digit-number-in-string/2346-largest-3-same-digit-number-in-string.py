class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans=max([ int(num[i:i+3]) if (len(set(num[i:i+3]))==1)  else -1 for i in range(len(num)-2) ])

        if ans==0: return "0"*3
        return str(ans) if ans!=-1 else ""
        