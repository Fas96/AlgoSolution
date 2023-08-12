class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxS=nums[0]
        gls=0
        
        for x in nums:
            gls+=x
            mxS=max(mxS,gls)
            gls=max(gls,0)
        return mxS