class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]  
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]  

         
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # DP iterations
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp0[i][j] = sum(dp1[i - k][j] for k in range(1, min(limit, i) + 1)) % mod
                dp1[i][j] = sum(dp0[i][j - k] for k in range(1, min(limit, j) + 1)) % mod

        return (dp0[zero][one] + dp1[zero][one]) % mod