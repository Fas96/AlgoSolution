class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        d = [0] * (n + 1)
        for x, y in edges:
            d[x] += 1
            d[y] += 1
        for i in range(1, n + 1):
            if d[i] == n - 1:
                return i
        