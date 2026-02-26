class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        given=int(s,2)
        while given!=1:
            if given%2==0:
                given=given//2 
            elif given%2!=0:
                given=given+1 
            ans+=1
        return ans
        