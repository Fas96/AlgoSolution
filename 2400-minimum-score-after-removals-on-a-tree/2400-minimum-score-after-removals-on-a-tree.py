class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        xorSubTree = [0] * n
        inTime = [0] * n
        outTime = [0] * n
        time = [0]
        def DFS(u, parent):
            xor = nums[u]
            time[0] += 1
            inTime[u] = time[0]
            for v in graph[u]:
                if v != parent:
                    xor ^= DFS(v, u)
            outTime[u] = time[0]
            xorSubTree[u] = xor
            return xor
        totalXor = DFS(0, -1)
        def find(u, v):
            return inTime[u] <= inTime[v] and outTime[v] <= outTime[u]
        subtreeRoots = []
        for u, v in edges:
            if inTime[u] > inTime[v]:
                subtreeRoots.append(u)
            else:
                subtreeRoots.append(v)

        minScore = float('inf')
        for i in range(len(subtreeRoots)):
            for j in range(i + 1, len(subtreeRoots)):
                u, v = subtreeRoots[i], subtreeRoots[j]
                if find(u, v):
                    a = xorSubTree[v]
                    b = xorSubTree[u] ^ xorSubTree[v]
                    c = totalXor ^ xorSubTree[u]
                elif find(v, u):
                    a = xorSubTree[u]
                    b = xorSubTree[v] ^ xorSubTree[u]
                    c = totalXor ^ xorSubTree[v]
                else:
                    a = xorSubTree[u]
                    b = xorSubTree[v]
                    c = totalXor ^ xorSubTree[u] ^ xorSubTree[v]
                score = max(a, b, c) - min(a, b, c)
                minScore = min(minScore, score)
        return minScore
