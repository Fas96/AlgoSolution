class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        forward=True 
        ans=1
        for i in range(time,0,-1):
            if forward:
                ans+=1
                if ans%n==0: forward=not forward
            else:
                ans-=1
                if ans==1: forward=not forward
       
        return ans