class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3: return n-1
        prd=1
        while n>4:
            prd*=3
            n-=3
        prd*=n
        
        return prd
        