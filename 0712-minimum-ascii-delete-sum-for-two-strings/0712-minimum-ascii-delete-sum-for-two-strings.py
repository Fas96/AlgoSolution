class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return sum(map(ord, s2[j:]))
            if j == n:
                return sum(map(ord, s1[i:]))
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            return min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))

        return dp(0, 0)