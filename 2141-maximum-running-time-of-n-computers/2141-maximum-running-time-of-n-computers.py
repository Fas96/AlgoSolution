class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(t):
            return sum(min(t, v) for v in batteries) >= n * t

        lo, hi = 0, sum(batteries) // n
        while lo < hi:
            mid = (hi + lo) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo if check(lo) else lo - 1