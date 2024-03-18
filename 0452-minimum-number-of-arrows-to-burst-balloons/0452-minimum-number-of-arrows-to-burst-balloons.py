class Solution:
    def findMinArrowShots(self, P: List[List[int]]) -> int:
        an=1
        P=sorted(P,key=lambda x: x[0])
        start,end=P[0][0],P[0][1]
 
        for i in range(1,len(P)):
            if P[i][0]>end:
                an+=1
                end=P[i][1]
            else:
                end = min(end, P[i][1])
        return an
    