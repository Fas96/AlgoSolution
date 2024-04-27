class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0
            ans = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[j]:
                    delta = abs(k - i)
                    steps = min(delta, len(ring) - delta)
                    ans = min(ans, steps + dp(k, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0) + len(key)