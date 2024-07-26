class Solution:
    def countPrimes(self, n: int) -> int:
        def soe(n): 
            is_prime = [True] * (n + 1) 
            if n >= 0: is_prime[0] = False
            if n >= 1: is_prime[1] = False 
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime 
        flg = soe(n)
         
        return len([b for b in flg[:len(flg)-1] if b]) 