class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i, s):
            if i == 0: return 1
            return dp(i-1, -s) + 1 if (nums[i] - nums[i-1])*s < 0 else dp(i-1, s)
            
        return max(dp(len(nums)-1, -1), dp(len(nums)-1, 1))