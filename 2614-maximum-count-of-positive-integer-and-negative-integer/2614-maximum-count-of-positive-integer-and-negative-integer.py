class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(x<0 for x in nums),sum(x>0 for x in nums))
        