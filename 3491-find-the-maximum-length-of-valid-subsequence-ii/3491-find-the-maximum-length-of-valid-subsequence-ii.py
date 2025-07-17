from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * n for _ in range(k)]
        max_sub = 1
        for i in range(1, n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                dp[mod][i] = max(dp[mod][i], 1 + dp[mod][j])
                max_sub = max(max_sub, dp[mod][i])
        return max_sub