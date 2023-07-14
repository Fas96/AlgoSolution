class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        for u, v in connections:
            adjList[u].append((v, 1))
            adjList[v].append((u, 0))
        print(adjList)
        visited = set()
        res = 0
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor, direction in adjList[node]:
                if neighbor not in visited:
                    res += direction
                    queue.append(neighbor)
        return res
        