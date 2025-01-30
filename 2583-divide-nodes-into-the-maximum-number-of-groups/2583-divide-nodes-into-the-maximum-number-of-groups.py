
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for src, tar in edges:
            adjList[src].append(tar)
            adjList[tar].append(src)
        
        visited = set()

        def getNodesInConnectedComponent(src):  
            visited.add(src)
            queue = deque([src])
            nodes = {src}  
            while queue:
                curr = queue.popleft()
                for nb in adjList[curr]:
                    if nb not in visited: 
                        visited.add(nb) 
                        nodes.add(nb)
                        queue.append(nb)
            return nodes

        def getMaxGroup(src):
            q = deque([(src, 1)])
            d = {src: 1}
            while q:
                curr, length = q.popleft()
                for nb in adjList[curr]:
                    if nb in d:
                        if d[nb] == length:  # Check bipartite condition
                            return -1
                    else:
                        d[nb] = length + 1
                        q.append((nb, length + 1))
            return max(d.values())

        res = 0
        for i in range(1, n + 1):
            if i in visited:
                continue
            nodes = getNodesInConnectedComponent(i)
            maxLen = 0
            for node in nodes:
                currLen = getMaxGroup(node)
                if currLen == -1:  # If not bipartite, return -1
                    return -1
                maxLen = max(maxLen, currLen)
            res += maxLen
        
        return res