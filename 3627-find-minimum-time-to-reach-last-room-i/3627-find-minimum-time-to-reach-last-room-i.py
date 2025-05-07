import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0]) if n > 0 else 0
        if n == 0 or m == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        heap = []
        heapq.heappush(heap, (moveTime[0][0], 0, 0))
        
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = moveTime[0][0]
        
        while heap:
            current_time, x, y = heapq.heappop(heap)
            if x == n - 1 and y == m - 1:
                return current_time
            if current_time > dist[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_time = max(current_time , moveTime[nx][ny])+ 1
                    if dist[nx][ny] >new_time :
                        dist[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, nx, ny))
        return dist[n-1][m-1] if dist[n-1][m-1] != float('inf') else -1