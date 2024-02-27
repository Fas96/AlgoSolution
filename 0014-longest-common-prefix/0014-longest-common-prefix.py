class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ab=sorted(strs,key=len)
         
        ans=""
        for x in ab[0]: 
            if all(ux.startswith(ans+x) for ux in strs): 
                ans+=x
            
        
        return ans
        