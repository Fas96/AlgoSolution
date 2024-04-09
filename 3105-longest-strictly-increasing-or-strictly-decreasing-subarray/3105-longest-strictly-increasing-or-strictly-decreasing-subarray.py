class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('-inf')
        if len(set(nums))==1: return 1
        for i in range(n):
            cnt=1
            for j in range(i+1,n):
                if nums[j-1]>nums[j]:cnt+=1 
                else:break
            ans=max(cnt,ans)
        for i in range(n):
            cnt=1
            for j in range(i+1,n):
                if nums[j-1]<nums[j]:cnt+=1
                else:break
            ans=max(cnt,ans)
        return ans
                
                
        