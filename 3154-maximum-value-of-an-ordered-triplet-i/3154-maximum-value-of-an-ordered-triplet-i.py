class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float("-inf")
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j < k:
                        ans=max(ans,(nums[i] - nums[j]) * nums[k])
        return ans if ans>0 else 0
        