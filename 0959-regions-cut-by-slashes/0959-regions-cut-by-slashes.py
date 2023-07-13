class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = 4 * n * n
        uf = [i for i in range(m)]

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                idx = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(idx, idx + 3)
                    union(idx + 1, idx + 2)
                elif grid[i][j] == '\\':
                    union(idx, idx + 1)
                    union(idx + 2, idx + 3)
                else:
                    union(idx, idx + 1)
                    union(idx + 1, idx + 2)
                    union(idx + 2, idx + 3)
                if i < n - 1:
                    union(idx + 2, idx + 4 * n)
                if j < n - 1:
                    union(idx + 1, idx + 4 + 3)
        return sum([1 for i in range(m) if find(i) == i])
        