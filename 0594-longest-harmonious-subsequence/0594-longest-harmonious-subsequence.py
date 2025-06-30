class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        ans=0 
        while l< len(nums):
            if nums[l]+1 not in nums:
                l+=1
                continue
            end=bisect_right(nums,nums[l]+1)-l 
            ans=max(ans,end) 
            l+=1
        return ans 