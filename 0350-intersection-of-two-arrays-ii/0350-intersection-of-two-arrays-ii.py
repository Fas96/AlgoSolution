class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f=Counter(nums1)
        ans=[]
        for val in nums2:
            if (val in f) and (f[val]):
                ans+=[val]
                f[val]-=1
        return ans

        