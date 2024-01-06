from bisect import bisect, bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def findMaxProfit(curr):
            print(curr)
            if curr >= n: return 0
            if memo[curr] != -1: return memo[curr]
            next_idx = bisect_left(startTime, jobs[curr][1])
            max_profit = max(findMaxProfit(curr + 1), jobs[curr][2] + findMaxProfit(next_idx))
            memo[curr] = max_profit
            return memo[curr]
        
        n = len(startTime)
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append([s, e, p])
        jobs.sort()
        startTime.sort()
        memo = [-1] * n
        return findMaxProfit(0)