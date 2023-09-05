class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L,R=0,len(nums)-1
        while L< R:
            if nums[L]+nums[R]>target:
                R-=1
            elif nums[L]+nums[R]<target:
                L+=1
            else:
                return [L+1,R+1]
        return [-1,-1]