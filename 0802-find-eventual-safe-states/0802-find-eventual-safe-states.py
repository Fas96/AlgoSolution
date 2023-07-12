class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        N = len(graph)
        safeNode = {}

        def dfs(idx):
            if idx in safeNode:
                return safeNode[idx]
            safeNode[idx] = False
            for nei in graph[idx]:
                if not dfs(nei):
                    return safeNode[idx]
            safeNode[idx] = True
            return True
        return [i for i in range(N) if dfs(i)]