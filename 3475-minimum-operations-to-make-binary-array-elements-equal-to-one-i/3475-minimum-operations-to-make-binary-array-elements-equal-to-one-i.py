class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans,i,n=0,0,len(nums)
        for i in range(n-2):
            if nums[i]^1:
                nums[i], nums[i + 1], nums[i + 2] = nums[i] ^ 1, nums[i + 1] ^ 1, nums[i + 2] ^ 1
                ans+=1
        return -1 if 0 in nums[n-2:] else ans
        