class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        for _ in range(len(nums)-k):
            nums.remove(min(nums))
        return nums