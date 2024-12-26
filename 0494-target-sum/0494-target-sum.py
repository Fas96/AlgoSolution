class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hsh={}
        def recursive(idx,cs):
            if idx==len(nums):
                return 1 if cs==target else 0
            if (idx,cs) in hsh:
                return hsh[(idx,cs)]
            hsh[(idx,cs)]=recursive(idx+1,cs+nums[idx])+recursive(idx+1,cs-nums[idx])
            return hsh[(idx,cs)]



        return recursive(0,0)