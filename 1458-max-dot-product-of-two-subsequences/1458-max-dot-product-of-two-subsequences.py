class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[-inf] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                mul_num = nums1[i] * nums2[j]
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], mul_num, dp[i][j] + mul_num)
        return dp[-1][-1]