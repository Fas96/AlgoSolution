class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n)]
        self.rank = [1] * n
        self.group = [1] * n
               
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            self.group[x] += 1
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.group[y] += self.group[x]
            self.group[x] = 0
        else:
            self.parent[y] = x
            self.group[x] += self.group[y]
            self.group[y] = 0
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
       
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m+n)
        for i, j in product(range(m), range(n)):
            if grid[i][j]:
                uf.union(i, j+m)
        return sum(g-1 for g in uf.group if g > 2)