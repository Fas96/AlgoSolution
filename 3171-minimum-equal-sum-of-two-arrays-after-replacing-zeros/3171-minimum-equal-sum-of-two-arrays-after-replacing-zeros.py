class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        if (0 not in nums1) or  ( 0 not in nums2):
            return -1
 
        return  max(sum(nums1)+nums1.count(0),sum(nums2)+nums2.count(0))