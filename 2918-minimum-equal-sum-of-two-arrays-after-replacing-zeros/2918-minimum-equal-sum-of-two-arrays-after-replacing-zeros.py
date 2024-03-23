class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        countZeroes1,countZeroes2,sum1,sum2=nums1.count(0),nums2.count(0),sum(nums1),sum(nums2)
            
        sum1+=countZeroes1
        sum2+=countZeroes2
        if (sum1 < sum2 and countZeroes1==0) or (sum2 < sum1 and countZeroes2==0):
            return -1 
        return  max(sum1,sum2)