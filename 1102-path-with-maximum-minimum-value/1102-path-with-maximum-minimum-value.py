class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int: 
        m, n = len(grid), len(grid[0])
        pq = [(-grid[0][0], 0, 0)]
        visited = set()
        p=[]
        
        while pq:
            val, i, j = heapq.heappop(pq)
            if (i, j) in visited: continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:  
                return -val 
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    newval = max(val, -grid[ni][nj])
                    
                    heapq.heappush(pq, (newval, ni, nj))
  
        return -1