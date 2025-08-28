class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        for d in range(n-2, -1, -1):
            diag=sorted(grid[i][i+d] for i in range(n-d))
            for i in range(n-d):
                grid[i][i+d]=diag[i]
        for d in range(n):
            diag=sorted((grid[j+d][j] for j in range(n-d)), reverse=True)
            for j in range(n-d):
                grid[j+d][j]=diag[j]
        return grid
        