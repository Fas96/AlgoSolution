class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for i in edges:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        n=len(edges)
        for k,v in g.items():
            if len(v)==n:
                return k

        return -1
        