class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
       
        def prime_sieve(n): 
            flag = n % 6 == 2
            sieve = bytearray((n // 3 + flag >> 3) + 1)
            for i in range(1, int(n**0.5) // 3 + 1):
                if not (sieve[i >> 3] >> (i & 7)) & 1:
                    k = (3 * i + 1) | 1
                    for j in range(k * k // 3, n // 3 + flag, 2 * k):
                        sieve[j >> 3] |= 1 << (j & 7)
                    for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                        sieve[j >> 3] |= 1 << (j & 7)
            return sieve
        def prime_list(n): 
            res = []
            if n > 1:
                res.append(2)
            if n > 2:
                res.append(3)
            if n > 4:
                sieve = prime_sieve(n + 1)
                res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
            return res
        ll=prime_list(n)
        return len(ll)-1 if ll[-1]==n else len(ll)
        