class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        visited = [0] * N
        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 2
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 1
            return True
        return [i for i in range(N) if dfs(i)]