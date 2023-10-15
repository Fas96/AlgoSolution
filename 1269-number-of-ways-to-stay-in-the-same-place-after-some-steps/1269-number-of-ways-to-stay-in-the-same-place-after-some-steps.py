class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD=10**9+7
        @cache
        def df(i, s):
            
            if i >= arrLen or i < 0 or i > steps - s:
                return 0

            if s == steps:
                return 1 if i == 0 else 0

            return df(i, s + 1) + df(i + 1, s + 1) + df(i - 1, s + 1)
        
        return df(0, 0) % (MOD)
        