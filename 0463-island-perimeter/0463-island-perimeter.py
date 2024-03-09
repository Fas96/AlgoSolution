class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        M,N=len(grid),len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    ans+=4
                    if i and grid[i-1][j]:
                        ans-=2
                    if j and grid[i][j-1]:
                        ans-=2
        return ans
                    
        
        