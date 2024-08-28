class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid2, x, y): 
            if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]) or grid2[x][y] == 0:
                return 
            if grid1[x][y] !=1:
                nonlocal flag
                flag=False
            
            grid2[x][y] = 0  
            dfs(grid2, x-1, y)
            dfs(grid2, x+1, y)
            dfs(grid2, x, y-1)
            dfs(grid2, x, y+1)

        ans = 0 
        for i in range(len(grid2)):
                for j in range(len(grid2[0])):
                    if grid2[i][j] == 1:
                        flag=True
                        dfs(grid2, i, j) 
                        if flag: ans+=1
        return ans