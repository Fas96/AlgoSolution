class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def rec(idx,curSum):
            if idx==len(nums):
                return 1 if curSum==target else 0
            if (idx,curSum) in dp:
                return dp[(idx,curSum)]
            add=rec(idx+1,curSum+nums[idx])
            sub=rec(idx+1,curSum-nums[idx])
            dp[(idx,curSum)]=add+sub
            return add+sub
        return rec(0,0)
        