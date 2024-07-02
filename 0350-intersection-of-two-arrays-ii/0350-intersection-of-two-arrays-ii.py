class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        return [k for k, v in (Counter(nums1) & Counter(nums2)).items() for _ in range(v)]

        