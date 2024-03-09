class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ll=Counter(nums1)
        for x in nums2:
            if x in ll:
                return x
        return  -1
        