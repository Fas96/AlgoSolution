class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod=10**9+7
        def powMod(x, exp):
            if exp==0: return 1
            y=x if (exp&1)==1 else 1
            return y*powMod((x*x)%Mod, exp>>1)%Mod
        n0=(n+1)//2
        n1=n-n0
        return powMod(5, n0)*powMod(4, n1)%Mod    