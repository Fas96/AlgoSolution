class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minArr=[]
        for x in  timePoints:
            h,m= map(int, x.split(":"))
            minArr.append(h*60+m)
        minArr.sort()
        ans=float('inf')
        for i in range(1,len(minArr)):
            ans=min(ans,minArr[i]-minArr[i-1])
            
        ans=min(ans,minArr[0]+1440-minArr[-1])
        
        return ans