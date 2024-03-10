class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=list(accumulate(nums, operator.mul)) 
        postfix=1
        answer=[1]+pf
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]
        
            
            
        return answer[:-1]