class Solution:
    def timetaken(self, dist, speed, k):
        time = 0
        for i in dist[:-1]: 
            time += math.ceil(i/speed)
        time += dist[-1]/speed
        return time
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        res = -1
        lo, hi = 1, 10**7 
        
        while lo <= hi:
            mid = (lo+hi)//2
            time = self.timetaken(dist, mid, hour) 
            if time <= hour:
                res = mid
                hi = mid-1
            elif time > hour:
                lo = mid+1
        
        return res
     
        