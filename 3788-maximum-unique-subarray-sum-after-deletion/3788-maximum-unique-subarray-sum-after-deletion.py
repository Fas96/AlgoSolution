class Solution:
    def maxSum(self, nums: List[int]) -> int:
        val=set(nums)  
        pos=sum(g for g in val if g>0  )
        if  pos>0:
            return  pos
        return max(val)
         