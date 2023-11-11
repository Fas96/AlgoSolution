class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges: 
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        dist = [inf]*len(self.graph)
        dist[node1] = 0 
        while pq: 
            cost, u = heappop(pq)
            if u == node2: return cost
            for v, w in self.graph[u]: 
                if cost + w < dist[v]: 
                    dist[v] = cost + w
                    heappush(pq, (cost + w, v))
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)