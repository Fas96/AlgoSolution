class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n<=1:return 1
        ans=0
        for i in range(1,n*2):
            if i%2==1: ans+=1
        return ans-1
        