class Solution(object):
    def findKthLargest(self, nums, k):
        # nums.sort()
        return sorted(nums)[-k]
        