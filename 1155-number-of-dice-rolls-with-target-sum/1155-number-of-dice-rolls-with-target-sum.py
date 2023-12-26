class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n * k or target < n: return 0
        if n == 0: return target == 0
        return sum(self.numRollsToTarget(n-1, k, target-i) for i in range(1, k+1))%(10**9+7)      