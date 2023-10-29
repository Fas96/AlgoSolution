class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        tmp = log2(buckets)
        t = ceil(minutesToTest/minutesToDie)

        if t == 1: return ceil(tmp)
        return ceil(tmp / log2(t+1)) 
        