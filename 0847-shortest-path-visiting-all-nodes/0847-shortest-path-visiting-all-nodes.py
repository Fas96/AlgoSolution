class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        init = [(i, 0 | (1 << i)) for i in range(n)]
        q, seen = deque(init), set(init)
        steps, final_state = 0, (2 ** n) - 1

        while q:
            for _ in range(len(q)):
                i, path = q.popleft()
                if path == final_state:
                    return steps
                for j in graph[i]:
                    new_state = (j, path | (1 << j))
                    if new_state in seen: continue
                    seen.add(new_state)
                    q.append(new_state)
            steps += 1

        return 0
        