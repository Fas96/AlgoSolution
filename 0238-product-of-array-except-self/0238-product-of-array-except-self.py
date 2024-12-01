class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lf=[1]*n
        rt=[1]*n
        an=[]
        for i in range(1, n):
            lf[i] = nums[i-1] * lf[i - 1]
        for i in range(n-2,-1,-1): 
            rt[i]=nums[i+1]*rt[i+1]
        for i in range(n):
            an.append(rt[i]*lf[i])
         
        return an
        
        