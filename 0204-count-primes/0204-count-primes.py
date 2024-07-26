class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve_of_eratosthenes(n): 
            is_prime = [True] * (n + 1) 
            if n >= 0: is_prime[0] = False
            if n >= 1: is_prime[1] = False 
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime 
        prime_flags = sieve_of_eratosthenes(n)
         
        return len([i for i, prime in enumerate(prime_flags[:len(prime_flags)-1]) if prime]) 