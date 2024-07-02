class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f=Counter(nums2)
        ans=[]
        for val in nums1:
            if (val in f) and (f[val]):
                ans+=[val]
                f[val]-=1
        return ans

        