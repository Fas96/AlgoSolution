class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bs(nums):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2 
                if nums[m]<0:
                    l=m+1
                else:
                    r=m-1 
            return l
        neg=bs(nums)
        return max(neg,len(nums)-neg-(nums.count(0)))
        