class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        dp=[]
        for n in nums:
            idx=bisect.bisect_left(dp,n)
            if idx < len(dp):
                dp[idx]=n
            else:
                dp.append(n)
        return len(dp)
        