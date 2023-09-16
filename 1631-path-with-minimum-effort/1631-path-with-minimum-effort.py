class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        visited = set()
         
        while pq:
            effort, i, j = heapq.heappop(pq)
            if (i, j) in visited: continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1: return effort
          
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    newEffort = max(effort, abs(heights[i][j] - heights[ni][nj]))
                    
                    heapq.heappush(pq, (newEffort, ni, nj))
         
        return -1