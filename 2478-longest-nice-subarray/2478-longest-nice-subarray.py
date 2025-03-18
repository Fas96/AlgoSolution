from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1  
        end,    n = 0,  len(nums)
        used_bits = 0   

        for s in range(n):
            while (used_bits & nums[s]) != 0:  
                used_bits ^= nums[end]  
                end += 1   
            used_bits |= nums[s]  
            ans = max(ans,s - end + 1) 
        
        return ans
