class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        need = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for i in range(rows - 2):
            for j in range(cols - 2):
                if (set([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i][j+1], grid[i+1][j+2], grid[i][j+2], grid[i+1][j+1], grid[i+2][j+2], grid[i+2][j+1]]) == need and 
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] ==
                    grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] ==
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] ==
                    grid[i][j] + grid[i+1][j] + grid[i+2][j] ==
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] ==
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] ==
                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] ==
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]):
                        res += 1
        return res