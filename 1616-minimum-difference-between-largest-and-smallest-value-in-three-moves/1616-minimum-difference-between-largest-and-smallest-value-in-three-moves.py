class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0 
        return min([mx-mn for mn, mx in zip(nsmallest(4, nums), nlargest(4, nums)[::-1])])