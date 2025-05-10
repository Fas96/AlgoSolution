 

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def sum_and_zero(nums):
            total_sum = 0
            zero_count = 0
            for num in nums:
                if num == 0:
                    zero_count += 1
                total_sum += num
            return (total_sum, zero_count)
        
        sum1, zero1 = sum_and_zero(nums1)
        sum2, zero2 = sum_and_zero(nums2)
        
        total1 = sum1 + zero1
        total2 = sum2 + zero2
        
        if total1 == total2:
            return total1
        
        if total1 < total2:
            if zero1 == 0:
                return -1
            return total2
        else:
            if zero2 == 0:
                return -1
            return total1