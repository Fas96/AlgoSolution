class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        prod=0
        nums1.sort(reverse=True)
        nums2.sort()
        
        for i in range(len(nums1)):
            prod+=(nums1[i]*nums2[i])
    
        return prod
        
        