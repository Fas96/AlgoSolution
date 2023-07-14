class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        n = len(points)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    g[i].append((abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1]), j))
    
        heap = [(0,0)]
        ans = 0
        visited = set()
        while heap:
            weight, to = heapq.heappop(heap)
            if to in visited:
                continue
            ans += weight
            visited.add(to)
    
            for cost, nei in g[to]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))
    
        return ans
        