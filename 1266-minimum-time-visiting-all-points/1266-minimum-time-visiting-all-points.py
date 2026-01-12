class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int: 
        ans=0
        x,y=points[0]
        for x1,y1 in points[1:]:
            ans+=max(abs(y-y1),abs(x-x1))
            x,y=x1,y1 
        return ans
        