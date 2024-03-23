class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
      
        sum1,sum2=sum(nums1),sum(nums2)
            
        sum1+=nums1.count(0)
        sum2+=nums2.count(0)
        if (sum1 < sum2 and nums1.count(0)==0) or (sum2 < sum1 and nums2.count(0)==0):
            return -1 
        return  max(sum1,sum2)