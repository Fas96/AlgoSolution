class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end,cnt=-pow(5,10),0
        
        for s,e in sorted(intervals,key=lambda k:k[1]):
            if s>=end:
                end=e
            else:
                cnt+=1 
        return cnt
    
        