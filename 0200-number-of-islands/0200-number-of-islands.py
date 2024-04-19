class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nI=0
        N=len(grid)
        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return
            grid[i][j]='0'
            for ni,nj in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(grid,i+ni,j+nj) 
                
        for i in range(N):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    nI+=1
                    dfs(grid,i,j)
        
        return nI
        