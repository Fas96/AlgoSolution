class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            if (m != 0) and (n != 0):
                for i in range(n - 1, -1, -1):
                    nums1[m+i] = nums2[i]
                nums1.sort()
        return nums1
                
            
        