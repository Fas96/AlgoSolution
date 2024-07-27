class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(original)):
            graph[original[i]].append((changed[i], cost[i]))
        cache = {}
        def dijkstra(src, des):
            if (src, des) in cache:
                return cache[(src, des)]
            heap = [(0, src)]
            cost_list = {c:inf for c in "abcdefghijklmnopqrstuvwxyz"}
            cost_list[src] = 0
            while heap:
                cur_cost, cur_node = heapq.heappop(heap)
                if cur_cost > cost_list[cur_node]:
                    continue
                if cur_node == des:
                    cache[(src, des)] = cur_cost
                    return cur_cost
                cost_list[cur_node] = cur_cost
                for next_node, next_cost in graph[cur_node]:
                    heapq.heappush(heap, (cur_cost + next_cost, next_node))
            cache[(src, des)] = -1
            return cache[(src, des)]
        res = 0
        for i in range(len(source)):
            local_dist = dijkstra(source[i], target[i])
            if local_dist == -1:
                return -1
            else:
                res += local_dist
        return res