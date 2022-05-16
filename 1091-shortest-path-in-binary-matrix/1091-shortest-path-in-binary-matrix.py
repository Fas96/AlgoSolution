class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
   
        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        queue = deque()
        queue.append([0, 0, 1])
        
        while len(queue) > 0:
            x, y, currLength = queue.popleft()
            
            if x < 0 or x >= len(grid):
                continue
            if y < 0 or y >= len(grid):
                continue
            if visited[x][y] == 1:
                continue
            if grid[x][y] == 1:
                continue
            if x == len(grid) - 1 and y == len(grid) - 1:
                if grid[x][y] == 0:
                    return currLength
                continue
                
            visited[x][y] = 1
                
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    queue.append([i, j, currLength+1])
                    
        return -1
                