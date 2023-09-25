class Solution:
    def findTheDifference(self, s: str, t: str) -> str: 
        mt={}
        for c in t:
            if c in mt:
                mt[c]+=1
            else:
                mt[c]=1
        for c in s:
            mt[c]-=1
        
        ans=""
        for k,v in mt.items():
            if v>0:
                ans+=k
        
            
        return ans