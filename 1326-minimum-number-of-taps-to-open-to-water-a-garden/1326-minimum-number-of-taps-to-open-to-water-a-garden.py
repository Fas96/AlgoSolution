class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if len(ranges)==0: return -1
        if len(set(ranges))==1 and ranges[0]==0:  return -1
        
        tem=[i for i in range(len(ranges))]
        for i in range(len(ranges)):
            tem[max(i - ranges[i],0)]= i + ranges[i]
        
        
        
        ans,curf,nextf=0,0,0
        
        for i in range(len(ranges)-1):
            if i > curf:
                return -1
            nextf=max(nextf,tem[i])
            if i ==curf:
                curf=nextf
                ans+=1
        if len(ranges)-1>curf:
            return -1
        return ans
        