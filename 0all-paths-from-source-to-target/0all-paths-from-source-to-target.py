class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                ans.append(path.copy())
                return
            for nrb in graph[node]:
                dfs(nrb)
                path.pop()

        ans = []
        path = []
        if not graph or len(graph) == 0:
            return ans
        dfs(0)
        return ans