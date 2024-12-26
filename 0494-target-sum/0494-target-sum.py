class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def rec(idx,curSum):
            if idx==len(nums):
                return 1 if curSum==target else 0
            if (idx,curSum) in dp:
                return dp[(idx,curSum)] 
            dp[(idx,curSum)]=rec(idx+1,curSum+nums[idx])+rec(idx+1,curSum-nums[idx])
            return dp[(idx,curSum)]
        return rec(0,0)
        