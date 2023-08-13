class Solution:
    def validPartition(self, nums: List[int]) -> bool: 
        n=len(nums)
        @cache
        def valid(i):
            if i==n:
                return True
            if i+1<n and nums[i]==nums[i+1] and valid(i+2):
                return True
            if i+2<n and (nums[i]==nums[i+1]==nums[i+2] or nums[i]==nums[i+1]-1 and nums[i+1]==nums[i+2]-1) and valid(i+3):
                return True

        return valid(0)
        