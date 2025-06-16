 

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        first = float('inf')
        second = float('inf')
        mx = -1   
        for x in nums:
            if x <= first:
                first = x
                second = float('inf')  
            else:
                if x < second:
                    second = x   
                mx = max(mx, x - first)  
        
        return mx if mx != 0 else -1   