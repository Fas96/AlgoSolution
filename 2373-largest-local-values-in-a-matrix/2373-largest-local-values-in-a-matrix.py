class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        maxLocal=[[float('-inf') for x in range(n-2)] for y in range(n-2)] 
        for i in range(n-2):
            for j in range(n-2): 
                for k in range(3):
                    for m in range(3):
                        maxLocal[i][j]=max(maxLocal[i][j],grid[i+k][j+m]) 
        return maxLocal
        