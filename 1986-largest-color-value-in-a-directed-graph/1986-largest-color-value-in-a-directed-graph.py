class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        revGraph = defaultdict(list)


        colorDict = defaultdict(int)
        indegrees = defaultdict(int)

        uniqueColors = list(set(colors))
        numColors = len(uniqueColors)
        maxNode = 0

        if len(edges) == 0:
            return 1

        for l, r in edges:
            graph[l].append(r)
            revGraph[r].append(l)

            if l > maxNode:
                maxNode = l
            if r > maxNode:
                maxNode = r

            indegrees[r] += 1
            

        dp = [[0] * numColors for _ in range(maxNode + 1)]
        
        for node in range(len(uniqueColors)):
            colorDict[uniqueColors[node]] = node
        
        q = deque()
        for node in graph:
            if indegrees[node] == 0:
                q.append(node)
                dp[node][colorDict[colors[node]]] = 1
        
        traversed = []
        while q:
            curr = q.popleft()
            traversed.append(curr)

            currColor = colors[curr]
            colorIx = colorDict[currColor]

            maxVal = -1
            for prev in revGraph[curr]:
                for ix in range(numColors):
                    dp[curr][ix] = max(dp[curr][ix], dp[prev][ix])
                maxVal = max(maxVal, dp[prev][colorIx])
            
            dp[curr][colorIx] = maxVal + 1 if maxVal != -1 else 1

            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        maxVal = max([max(k) for k in dp])
        return maxVal if len(traversed) == maxNode + 1 else -1
