class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(r,c,vis):
            if (r<0 or c<0 or (r >= len(grid)) or  (c>=len(grid[0])) or( (r,c) in vis)) or grid[r][c]==0:
                return 
            vis.add((r,c))
            neighbor=[[r+1,c],[r,c+1],[r,c-1],[r-1,c]]
            for nr,nc in neighbor:
                dfs(nr,nc,vis) 
        def countIslands():
            res=0
            vis = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] and (i,j) not in vis:
                        dfs(i,j,vis)
                        res+=1
            return res
      
        if countIslands()!=1:
            return 0
          
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                grid[i][j]=0
                if countIslands()!=1:
                    return 1
                grid[i][j]=1
        return 2
