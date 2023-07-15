class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return 0 
            ans = dp(i + 1, k)
             
            next_i = bisect_left(events, [events[i][1] + 1])
            ans = max(ans, events[i][2] + dp(next_i, k - 1))
            return ans
        return dp(0, k)
        