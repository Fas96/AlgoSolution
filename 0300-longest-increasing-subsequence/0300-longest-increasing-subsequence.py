class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        LIS=[1]*(len(nums))
        for idx in range(len(nums)-1,-1,-1):
            for jdx in range(idx+1,len(nums)):
                if nums[idx]<nums[jdx]:
                    LIS[idx]=max(LIS[idx],1+LIS[jdx])
        return max(LIS)
#         dp=[]
#         for n in nums:
#             idx=bisect.bisect_left(dp,n)
#             if idx < len(dp):
#                 dp[idx]=n
#             else:
#                 dp.append(n)
#         return len(dp)
        