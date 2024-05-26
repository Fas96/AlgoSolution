class Solution:
    def checkRecord(self, n: int) -> int:
        attendance=['A','L','P']
        mod = 10**9 + 7
        T = [[1, 1], [1, 0], [0, 0]]
        for i in range(1, n):
            t_0_0 = (T[0][0] + T[1][0] + T[2][0]) % mod
            t_0_1 = (t_0_0 + T[0][1] + T[1][1] + T[2][1]) % mod
            T = [[t_0_0, t_0_1], T[0], T[1]]
        return (sum(T[0]) + sum(T[1]) + sum(T[2])) % mod
        