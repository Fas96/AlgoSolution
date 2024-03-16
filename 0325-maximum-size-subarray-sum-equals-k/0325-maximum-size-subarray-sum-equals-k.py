class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans=0
        mp={0:-1}
        pf=0
        for i,x in enumerate(nums):
            pf+=x
            if pf-k in mp:
                ans=max(ans,i-mp[pf-k])
            mp.setdefault(pf,i)
           
                
        print(mp)
        return ans