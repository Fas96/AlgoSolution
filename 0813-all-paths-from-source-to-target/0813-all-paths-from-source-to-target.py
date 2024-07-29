class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])      
        res = []

        while  q:
            path = q.popleft()
            v = path[-1]
            for u in graph[v]:
                if u == n - 1:
                    res.append(path + [u])
                else:
                    q.append(path + [u])
        
        return res