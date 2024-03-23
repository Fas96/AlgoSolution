class DSU:
    def __init__(self):
        self.par = {}
        self.val = defaultdict(lambda: 1)

    def find(self, x: str) -> str:
        if x not in self.par:
            self.par[x] = x
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: str, y: str, q: float) -> None:
        # arbitrarily force all nodes in union find to point to py as
        # their new parent. Also, update everyone's value as well
        # according to the new ratio
        px, py = self.find(x), self.find(y)
        ratio = self.val[y] * q / self.val[x]
        for node, par in self.par.items():
            if par == px:
                self.par[node] = py
                self.val[node] *= ratio

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """LeetCode 399

        32 ms, faster than 87.32%
        """
        uf = DSU()
        for (x, y), v in zip(equations, values):
            uf.union(x, y, v)
        res = []
       
        for x, y in queries:
            if x not in uf.val or y not in uf.val or uf.find(x) != uf.find(y):
                res.append(-1.0)
            else:
                res.append(uf.val[x] / uf.val[y])
        return res