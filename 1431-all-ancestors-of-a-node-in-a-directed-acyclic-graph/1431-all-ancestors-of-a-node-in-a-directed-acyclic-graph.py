class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        for a,b in edges:
            g[b].append(a)
        ans=[set() for _ in range(n)]
        @cache
        def go(c):
            r=set([c])
            for u in g[c]:
                for v in go(u):
                    r.add(v)
            return r
        for i in range(n):
            ans[i]=set(go(i))
            ans[i].remove(i)
        for i in range(n):
            ans[i]=sorted(ans[i])
        return ans
        