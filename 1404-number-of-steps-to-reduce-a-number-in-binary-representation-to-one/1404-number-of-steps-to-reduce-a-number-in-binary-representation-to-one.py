class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        while int(s, 2)!=1:
            if int(s, 2)%2==0:
                s=bin(int(s, 2)//2).replace("0b", "") 
            elif int(s, 2)%2!=0:
                s=bin(int(s, 2)+1).replace("0b", "") 
            ans+=1
        return ans
        