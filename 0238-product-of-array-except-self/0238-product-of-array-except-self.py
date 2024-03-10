class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=list(accumulate(nums, operator.mul)) 
       
        suffix=1
        answer=[1]+pf
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer[:-1]