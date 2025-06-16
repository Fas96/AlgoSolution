 

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        first =second= float('inf')
        mx = -1   
        for x in nums:
            if x <= first:
                first = x
            mx = max(mx, x - first)  
        
        return mx if mx != 0 else -1   