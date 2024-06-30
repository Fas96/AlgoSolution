class UnionFind:
    
    def __init__(self, n: int):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.edges = [0 for _ in range(n)]
        self.group = [1 for _ in range(n)]
        
    def find(self, x: int) -> int:
        if x != self.root[x]: self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            self.edges[root_x] += 1
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
            self.edges[root_x] += self.edges[root_y] + 1
            self.group[root_x] += self.group[root_y]
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
            self.edges[root_y] += self.edges[root_x] + 1
            self.group[root_y] += self.group[root_x]
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
            self.edges[root_x] += self.edges[root_y] + 1
            self.group[root_x] += self.group[root_y]
    
    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
            

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        g = collections.defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            uf.union(u, v)
        for i in range(n):
            uf.find(i)
        
        s = set(uf.root)
        res = 0
        for x in s:
            v = uf.group[x]
            if uf.edges[x] == (v - 1) * v // 2: res += 1
        return res
            