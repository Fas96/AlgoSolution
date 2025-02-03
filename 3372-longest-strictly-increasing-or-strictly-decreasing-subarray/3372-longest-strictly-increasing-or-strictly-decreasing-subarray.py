class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int: 
        idx,jdx, ans= 0,0,float('-inf')
        N=len(nums)
        while idx < N and jdx < N:
            while jdx + 1 < N and nums[jdx + 1] > nums[jdx]:
                jdx += 1
            ans = max(ans, jdx - idx + 1)
            jdx += 1
            idx = jdx
        idx = 0
        jdx = 0
        while idx < N and jdx < N:
            while jdx + 1 < N and nums[jdx + 1] < nums[jdx]:
                jdx += 1
            ans = max(ans, jdx - idx + 1)
            jdx += 1
            idx = jdx
        return ans