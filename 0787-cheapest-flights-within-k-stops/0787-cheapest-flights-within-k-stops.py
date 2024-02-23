class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for node, to, cost in flights:
            adj[node].append((to, cost))

        minCost = float('inf')
        costs = [float('inf')] * n

        q = collections.deque([(src, 0)])
        while q and k >=-1:
            for _ in range(len(q)):
                node, cost = q.popleft()

                if node == dst:
                    minCost = min(minCost, cost)
                    continue

                for n, c in adj[node]:
                    if cost+c > costs[n]: continue
                    costs[n] = cost+c
                    q.append((n, c+cost))
 
            k-=1

        return minCost if minCost != float('inf') else -1