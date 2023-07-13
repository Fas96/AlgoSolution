class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = defaultdict(int)
        for x, y in trust:
            d[x] -= 1
            d[y] += 1
        for i in range(1, n + 1):
            if d[i] == n - 1:
                return i
        return -1