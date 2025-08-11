class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD=10**9 + 7
        powers=[]
        ans=[]
        rep =1
        while n > 0:
            if n % 2 == 1:
                powers.append(rep)
            n //= 2
            rep *= 2
         
        for i,c in enumerate(queries):
            l,r=c[0],c[1]
            cur = 1
            for i in range(l, r + 1):
                cur = (cur * powers[i]) % MOD
            ans.append(cur)

        return ans
        