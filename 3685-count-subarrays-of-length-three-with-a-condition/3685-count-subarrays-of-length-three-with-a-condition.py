 
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        seen = set()
        
        for i in range(n - 2):
            subarray = tuple(nums[i:i+3])  # using tuple as it's hashable
            a, b, c = subarray
            if a + c == b / 2: 
                ans += 1
        return ans