class UnionFind:
    def __init__(self, N):
        self.parents = [x for x in range(N)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        ua = self.find(a)
        ub = self.find(b)

        self.parents[ua] = ub

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N: int, edges: List[List[int]]) -> List[List[int]]:
        """
        for each edge: O(E)
            see if this edge is in the MST
            calculate new MST (E log E) or (V^2)
        """
        E = len(edges)
        e = sorted(enumerate(edges), key=lambda x: x[1][2])

        # Kruskal's algorithm
        def mst(current_index, start):
            uf = UnionFind(N)
            count = 0
            total = 0

            if start:
                su, sv, sw = edges[current_index]
                uf.union(su, sv)
                total += sw
                count += 1

            for index, (u, v, w) in e:
                if index == current_index:
                    continue

                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    total += w
                    count += 1

                if count == N - 1:
                    break

            return total

        base_mst = mst(-1, False)
        critical = []
        pseudocritical = []

        for i in range(E):
            if mst(i, True) == base_mst:
                # this edge is part of at least one MST

                if mst(i, False) != base_mst:
                    critical.append(i)
                else:
                    pseudocritical.append(i)

        return [critical, pseudocritical]
