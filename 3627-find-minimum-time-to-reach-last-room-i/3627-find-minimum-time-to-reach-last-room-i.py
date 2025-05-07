import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        h = [(0, 0, 0)]
        dist = {(0, 0): 0}

        while h:
            t, x, y = heapq.heappop(h)
            if dist.get((x, y), float('inf')) < t:
                continue
            if x == n - 1 and y == m - 1:
                return t
            
            for u, v in ((x - 1, y), (x, y - 1),
                         (x + 1, y), (x, y + 1)):
                if 0 <= u < n and 0 <= v < m:
                    next_t = max(t, moveTime[u][v]) + 1
                    if dist.get((u, v), float('inf')) > next_t:
                        dist[(u, v)] = next_t
                        heapq.heappush(h, (next_t, u, v))