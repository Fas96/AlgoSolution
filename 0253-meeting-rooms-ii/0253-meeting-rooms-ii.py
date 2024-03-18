class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = cur = 0
        for i, v in sorted(x for i,j in intervals for x in [[i, 1], [j, -1]]):
            cur += v
            res = max(res, cur)
        return res
        