class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        isCachede=[[False]*col for _ in range(row)]
        cache=[[None]*col for _ in range(row)]
        
        def pathCount(x,y):
            if obstacleGrid[x][y]== 1:
                return 0
            if x==0 and y==0:
                return 1
            if isCachede[x][y]:
                return cache[x][y]
            path=0
            if x-1>=0:
                path+=pathCount(x-1,y)
            if y-1>=0:
                path+=pathCount(x,y-1)
            isCachede[x][y]=True
            cache[x][y]=path
            return path
        return pathCount(row-1,col-1)
                
        
        