class Solution:
    def climbStairs(self, n: int) -> int: 
         
        @cache
        def go(g):
            if g==1 or g==2:
                return g
            return go(g-1)+go(g-2)
        return go(n)
        