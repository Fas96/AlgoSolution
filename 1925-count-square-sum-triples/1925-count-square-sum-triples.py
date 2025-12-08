class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            for j in range(1,n+1): 
                c_squared = i**2 + j**2
                c = sqrt(c_squared) 
                if c == int(c) and c <= n:
                    ans += 1
        return ans
        