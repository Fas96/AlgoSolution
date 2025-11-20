from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        res = []
        res.append(intervals[0][1] - 1)
        res.append(intervals[0][1])
        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]
            last = res[-1]
            second_last = res[-2]
            if start > last:
                res.append(end - 1)
                res.append(end)
            elif start == last:
                res.append(end)
            elif start > second_last:
                res.append(end)
        return len(res)