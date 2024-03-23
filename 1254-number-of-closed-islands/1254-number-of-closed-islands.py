class UF:
    def __init__(self, size):
            self.root = [i for i in range(size)]
            self.rank = [1 for _ in range(size)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
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
        
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        zerosLocation = {}

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    zerosLocation[r, c] = len(zerosLocation)
        uf = UF(len(zerosLocation))

        for r, c in zerosLocation:
            if (r-1, c) in zerosLocation:
                uf.union(zerosLocation[r, c], zerosLocation[r-1, c])
            if (r, c-1) in zerosLocation:
                uf.union(zerosLocation[r, c], zerosLocation[r, c-1])
       
        S = {uf.find(x) for x in range(len(zerosLocation))}
        
        for r, c in zerosLocation:
            if r in {0, m-1} or c in {0, n-1}:
                S.discard(uf.find(zerosLocation[r, c]))

        return len(S)