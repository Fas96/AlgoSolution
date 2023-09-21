class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n.sort()
        if len(n)&1:
            return n[len(n)//2]
        else: 
            return ( n[len(n)//2]+n[(len(n)//2)-1])/2
        