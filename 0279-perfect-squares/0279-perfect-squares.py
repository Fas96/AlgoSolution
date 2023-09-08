class Solution:
    def numSquares(self, n: int) -> int:
        c={}
        def go(n):
            if n==0: return 0
            if n<0:return float("inf")
            if n in c: return c[n]
            mini = n 
            i = 1
            
            while i*i<=n:                                                 
                mini = min(mini, go(n-(i*i)))
                i+=1
            c[n]=mini+1
            return mini+1

        return go(n)
        