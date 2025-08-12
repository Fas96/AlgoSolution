class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        xpowers = [i**x for i in range(1, int(n**(1/x)) + 2) if i**x <= n]
        MOD = 10**9 + 7 
        m = len(xpowers)
        dp = [0] * (n + 1)
        dp[0] = 1   
        for num in xpowers:
            for j in range(n, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[n] % MOD