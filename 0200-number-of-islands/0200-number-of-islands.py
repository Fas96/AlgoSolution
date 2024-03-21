
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
                if rootX == rootY: return False
                self.root[rootX] = rootY
                return True

            def connected(self, x, y):
                return self.find(x) == self.find(y)
        DIR = [0, 1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        
        T = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0": continue
                T += 1
                curId = r * n + c
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    neiId = nr * n + nc
                    if uf.union(curId, neiId):
                        T -= 1
        return T