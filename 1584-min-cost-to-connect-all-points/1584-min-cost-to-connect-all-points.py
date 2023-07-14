class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manD(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        g= {(x,y): float('inf') if i else 0 for i,(x,y) in enumerate(points)}
        ans = 0
        while g:
            x,y = min(g, key=g.get)
            ans += g.pop((x,y))
            for (i,j) in g:
                g[(i,j)] = min(g[(i,j)], manD((x,y), (i,j)))
        return ans
        