class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        idxMin,idxMax,jdxMin,jdxMax=1000,-1000,1000,-1000
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:continue
                idxMin=min(idxMin,i)
                idxMax=max(idxMax,i)
                jdxMin=min(jdxMin,j)
                jdxMax=max(jdxMax,j)
        return (idxMax-idxMin+1)*(jdxMax-jdxMin+1)

             