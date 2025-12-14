class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        temp = [i for i, c in enumerate(corridor) if c == 'S']
        n = len(temp)
        if not n or n & 1:
            return 0

        res = 1
        for i in range(2, n - 1, 2):
            res *= temp[i] - temp[i - 1]

        return res % MOD