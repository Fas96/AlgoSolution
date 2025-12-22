class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                if all(s[i] >= s[j] for s in strs):
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
        return m - max(dp)