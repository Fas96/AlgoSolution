class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build_graph(times)
        min_time = self.dijkstra(graph, n, k)
        return self.calculate_max_time(min_time, n)
    
    def build_graph(self, times: List[List[int]]) -> defaultdict:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        return graph
    
    def dijkstra(self, graph: defaultdict, n: int, start: int) -> dict:
        pq = [(0, start)]
        min_time = {i: float('inf') for i in range(1, n+1)}
        min_time[start] = 0
        while pq:
            current_time, node = heapq.heappop(pq)
            if current_time > min_time[node]:continue
            for neighbor, time in graph[node]:
                new_time = current_time + time
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
        return min_time
    
    def calculate_max_time(self, min_time: dict, n: int) -> int:
        max_time = max(min_time.values())
        return max_time if max_time < float('inf') else -1