class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        d = defaultdict(int)
        for x, y in edges:
            d[x] += 1
            d[y] += 1
        for k, v in d.items():
            if v == n - 1:
                return k
        