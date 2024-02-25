class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        L,R,N=0,0,len(nums)
        ans=0
        curS=0 
        ac=accumulate(nums)
       
        mp={0:1}
        for x in ac:
            if x-k in mp:
                ans+=mp[x-k]
            mp[x]=mp.get(x,0)+1
            
        
        return ans
                
        