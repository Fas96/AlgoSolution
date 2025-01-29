class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        t = ''.join(map(chr, range(1001)))
        for u,v in e:
            if t[u] == t[v]:
                return [u, v]
                
            t = t.replace(t[u], t[v])