from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1  
        i, e, n = 0, 0, len(nums)
        used_bits = 0   

        for e in range(n):
            while (used_bits & nums[e]) != 0:  
                used_bits ^= nums[i]  
                i += 1  
            
            used_bits |= nums[e]  
            ans = max(ans, e - i + 1) 
        
        return ans
