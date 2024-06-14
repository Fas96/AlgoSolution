class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                continue
            
            add=abs(nums[i+1]-nums[i])+1
            ans+=(add)
            nums[i+1]+=add
        return ans
            
            
        