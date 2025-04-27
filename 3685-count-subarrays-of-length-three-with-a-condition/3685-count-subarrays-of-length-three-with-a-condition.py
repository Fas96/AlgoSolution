 
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums) 
        for i in range(n - 2): 
            a, b, c = tuple(nums[i:i+3]) 
            if a + c == b / 2: 
                ans += 1
        return ans