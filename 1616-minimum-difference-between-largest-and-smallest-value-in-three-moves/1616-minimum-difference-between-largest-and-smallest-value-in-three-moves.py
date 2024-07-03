class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=4:return 0
        if max(nums)-min(nums)<1:return max(nums)-min(nums)
        nums.sort() 
        ANS=[]
        for i in range(4):
            ANS+= [nums[n-4+i]-nums[i]]

         
        return min(ANS)