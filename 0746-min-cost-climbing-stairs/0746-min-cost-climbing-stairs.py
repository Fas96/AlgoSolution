class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def mtd(cost, n, memo):
            if n <= 1: return cost[n]
            if memo[n] != -1: return memo[n]
            memo[n] = min(mtd(cost, n-1, memo), mtd(cost, n-2, memo)) + cost[n]
            return memo[n]
        n = len(cost)
        memo = [-1] * n
        return min(mtd(cost, n-1, memo), mtd(cost, n-2, memo))