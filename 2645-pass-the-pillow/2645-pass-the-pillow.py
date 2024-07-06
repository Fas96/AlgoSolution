class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div=time//(n-1)
        if div& 1==0:
            return (time % (n - 1) + 1) 
        return (n - time % (n - 1))
        