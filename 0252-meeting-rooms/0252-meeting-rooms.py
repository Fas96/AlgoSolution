class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        n=len(intervals)
        for x in range(1,n):
            if intervals[x-1][1]>intervals[x][0]:
                return False
        return True
        