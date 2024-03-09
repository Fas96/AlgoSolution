class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ll=list(set(nums1) & set(nums2))
        if len(ll)==0: return -1
        return min(ll)
        