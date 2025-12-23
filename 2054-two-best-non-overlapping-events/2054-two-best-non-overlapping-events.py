class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        Time=[(0, 0, 0)]*(n*2)
        for i, (s,e,v) in enumerate(events):
            Time[2*i]=(s, False, v)
            Time[2*i+1]=(e, True, v)
        Time.sort()
        ans, maxV=0, 0
        for t, isEnd, v in Time:
            if isEnd: maxV=max(maxV, v)
            else: ans=max(ans, maxV+v)
        return ans