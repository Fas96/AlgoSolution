class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        total_operations = 0
        factor = 2
        while factor * factor <= n:
            while n % factor == 0:
                total_operations += factor
                n //= factor
            factor += 1
        
        if n > 1:
            total_operations += n
        
        return total_operations
        