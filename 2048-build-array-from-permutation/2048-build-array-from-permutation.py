class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i,v in enumerate(nums):
            ans[i]= nums[nums[i]]
        return ans