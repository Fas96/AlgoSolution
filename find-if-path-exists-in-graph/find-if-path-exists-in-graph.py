class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size

            def find(self, x):
                while x != self.root[x]:
                    x = self.root[x]
                return x

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1

            def connected(self, x, y):
                return self.find(x) == self.find(y)
        uf=UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        return uf.connected(source,destination)

