class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        endStart,cnt=float("-inf"),0
        for start,end in sorted(intervals,key=lambda x:x[1]):
            if start>=endStart:
                endStart=end
            else:
                cnt+=1
        return cnt
        