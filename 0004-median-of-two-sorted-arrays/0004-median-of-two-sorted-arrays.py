class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n.sort()
        return n[len(n)//2] if len(n)&1 else ( n[len(n)//2]+n[(len(n)//2)-1])/2
    
        