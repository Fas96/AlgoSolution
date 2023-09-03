class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def bt(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if j == n - 1 and 0 <= i < m - 1:
                return grid[i][j] + bt(i + 1, j)
            if i == m - 1 and 0 <= j < n - 1:
                return grid[i][j] + bt(i, j + 1)
            if 0 <= j < n - 1 and 0 <= i < m - 1:
                return grid[i][j] + min(bt(i + 1, j), bt(i, j + 1))
        return bt(0, 0)
        