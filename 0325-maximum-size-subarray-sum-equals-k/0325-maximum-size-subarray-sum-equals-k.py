class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans=0
        mp={0:-1}
        pf=list(accumulate(nums))
        for i,x in enumerate(nums):
            
            if pf[i]-k in mp:
                ans=max(ans,i-mp[pf[i]-k])
            mp.setdefault(pf[i],i)
       
        return ans