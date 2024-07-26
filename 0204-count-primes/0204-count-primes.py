class Solution:
    def countPrimes(self, n: int) -> int:
        def soe(n): 
            fl = [True] * (n + 1) 
            if n >= 0: fl[0] = False
            if n >= 1: fl[1] = False 
            for i in range(2, int(n**0.5) + 1):
                if fl[i]:
                    for j in range(i * i, n + 1, i):
                        fl[j] = False
            return fl 
        flg = soe(n)
         
        return len([b for b in flg[:len(flg)-1] if b]) 