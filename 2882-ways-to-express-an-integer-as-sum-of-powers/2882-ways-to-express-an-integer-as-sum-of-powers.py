class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        ans=1 if x==1 else 0
        xpowers = []
        i = 1
        while True:
            power = i ** x
            if power > n:
                break
            xpowers.append(power)
            i += 1
        MOD = 10**9 + 7  
        m = len(xpowers)
        dp = [0] * (n + 1)
        dp[0] = 1   
        for num in xpowers:
            for j in range(n, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        return dp[n] % MOD