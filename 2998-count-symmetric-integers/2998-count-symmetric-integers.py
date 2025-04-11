class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=0
        for x in range(low,high+1,1):
            N=len(str(x))
            if N%2==0:
                if sum([int(x) for x in str(x)[:N//2]])==sum([int(x) for x in str(x)[N//2:]]):
                    ans+=1
        return ans
                    
                
        