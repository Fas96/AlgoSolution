class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        d = {
            1: [[0, 1], [0, -1]],
            2: [[1, 0], [-1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[0, 1], [-1, 0]]
        }

        def dfs(i, j):
            visited[i][j] = True
            for x, y in d[grid[i][j]]:
                if 0 <= i + x < m and 0 <= j + y < n and not visited[i + x][j + y] and [-x, -y] in d[grid[i + x][j + y]]:
                    dfs(i + x, j + y)

        dfs(0, 0)
        return visited[m - 1][n - 1]