class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        return sum(max(abs(x2-x1), abs(y2-y1)) for (x1, y1), (x2, y2) in zip(p, p[1:]))