class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, m*n-1)]
        res = -1
        visited = set()
        while pq:
            cost, cell = heapq.heappop(pq)
            if cell in visited:
                continue
            visited.add(cell)

            if cell == 0:
                res = cost
                break
            row, col = cell//n, cell%n
            if row > 0 and cell-n not in visited:
                c = 0 if grid[row-1][col] == 3 else 1
                heapq.heappush(pq, (cost + c, cell-n))
            if col > 0 and cell-1 not in visited:
                c = 0 if grid[row][col-1] == 1 else 1
                heapq.heappush(pq, (cost + c, cell-1))
            if row < m-1 and cell+n not in visited:
                c = 0 if grid[row+1][col] == 4 else 1
                heapq.heappush(pq, (cost+c, cell+n))
            if col < n-1 and cell+1 not in visited:
                c = 0 if grid[row][col+1] == 2 else 1
                heapq.heappush(pq, (cost + c, cell+1))
                
        return res