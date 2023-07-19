class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        endStart,cnt=float("-inf"),0
        sortIntervals=sorted(intervals,key=lambda x:x[1])
        for interval in sortIntervals:
            if interval[0]>=endStart:
                endStart=interval[1]
            else:
                cnt+=1
        return cnt
        