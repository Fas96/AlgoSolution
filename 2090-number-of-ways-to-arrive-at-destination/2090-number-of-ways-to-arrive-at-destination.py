import heapq

MOD = 1000000007

class Solution:
    def countPaths(self, n, roads):
        adj = [[] for _ in range(n)]
        
        # Build the graph
        for u, v, wt in roads:
            adj[u].append((wt, v))
            adj[v].append((wt, u))
        
        dist = [float('inf')] * n
        dist[0] = 0
        
        ways = [0] * n
        ways[0] = 1
        
        pq = [(0, 0)]  # (distance, node)
        
        while pq:
            wt, node = heapq.heappop(pq)
            
            for newWt, newNode in adj[node]:
                if wt + newWt < dist[newNode]:
                    dist[newNode] = wt + newWt
                    heapq.heappush(pq, (dist[newNode], newNode))
                    ways[newNode] = ways[node]
                elif wt + newWt == dist[newNode]:
                    ways[newNode] = (ways[newNode] + ways[node]) % MOD
        
        return int(ways[n - 1] % MOD)