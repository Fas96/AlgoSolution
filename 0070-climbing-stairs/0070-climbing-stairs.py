class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n 
        @cache
        def dp(n):
            if n<=2:return n 
            return dp(n-1)+dp(n-2)
        return dp(n)