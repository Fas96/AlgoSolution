class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        L,R=0,len(nums)-1
        ans=0
        while L<=R:
            if nums[L]+nums[R]<target:
                ans+=(R-L)
                L+=1
            else:
                R-=1
        return ans
                
        