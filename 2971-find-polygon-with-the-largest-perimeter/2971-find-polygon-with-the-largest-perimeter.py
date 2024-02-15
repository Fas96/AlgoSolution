class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        NS=sum(nums)
        n=len(nums)
        for i in range(n-1,1,-1):
            NS-=nums[i]
            if NS>nums[i]:
                return NS+nums[i]
        return -1 