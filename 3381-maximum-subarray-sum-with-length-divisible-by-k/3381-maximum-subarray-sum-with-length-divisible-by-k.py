class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

         
        pf=0
        mx=float("-inf")
        minAr=[float("inf")]*k
        minAr[(k-1)%k]=0
        for i,v in enumerate(nums):
           pf+=v
           mx=max(mx,pf- minAr[i%k])
           minAr[i%k]=min(minAr[i%k],pf)
        return mx
        