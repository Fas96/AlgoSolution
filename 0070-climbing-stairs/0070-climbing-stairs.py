class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        first,second,ans=1,2,0
        for i in range(3,n+1):
            ans=first+second
            first,second=second,ans
        return ans