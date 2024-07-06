class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cLen = 2 * (n - 1) 
        T = time % cLen
        
        return T+1 if T < n else  n - (T - (n - 1))
        