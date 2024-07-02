class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f1=Counter(nums1)
        f2=Counter(nums2)
        
        return [k for k, v in (f1 & f2).items() for _ in range(v)]

        