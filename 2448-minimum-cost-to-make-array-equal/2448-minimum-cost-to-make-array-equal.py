class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid,tempSum,trackMid = sum(cost) / 2 ,0,0 
        
        for target, co in arr:
            trackMid=target
            tempSum += co
            if tempSum >= mid:break
         
                
        return sum(abs(trackMid - n) * c for n, c in arr)
        