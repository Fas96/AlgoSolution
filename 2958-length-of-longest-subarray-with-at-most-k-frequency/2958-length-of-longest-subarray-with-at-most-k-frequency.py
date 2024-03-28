class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f=defaultdict(int)
        w,ans=0,0 
        for i,n in enumerate(nums):
            f[n]+=1 
            while f[n]>k:
                f[nums[w]]-=1 
                w+=1 
            ans=max(ans,i-w+1)
        return ans