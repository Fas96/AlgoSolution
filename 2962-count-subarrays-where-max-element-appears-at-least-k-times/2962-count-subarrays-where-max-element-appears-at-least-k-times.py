class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx,w,ans,N=max(nums),0,0,len(nums)
        fx=defaultdict(int)
        for i,n in enumerate(nums):
            fx[n]+=1
            while fx[mx]>=k:
                ans=ans+N-i
                fx[nums[w]]-=1
                w+=1
        
        return ans
        