class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mx=-1
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]<k:
                    mx=max(mx,nums[i]+nums[j])
        return mx
        