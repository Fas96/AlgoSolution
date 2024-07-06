class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cLen = 2 * (n - 1) 
        T = time % cLen
         
        if T < n: 
            return T + 1
        else: 
            return n - (T - (n - 1))
        