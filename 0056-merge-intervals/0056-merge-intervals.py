class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        if len(intervals)<2: return intervals
        ans=[]
        start,end=intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if end>=intervals[i][0]:
                end=max(end,intervals[i][1])
            else:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            
        ans.append([start,end])
        return ans
        