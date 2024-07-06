class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cLen = 2 * (n - 1) 
        T =k % cLen
        
        return T if T < n else  n - (T - (n - 1))-1