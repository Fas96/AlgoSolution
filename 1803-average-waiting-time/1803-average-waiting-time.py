class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
       
        w=0
        ans=0.0
        for a,b in customers:
            if a>w:
                ans+=b
                w=a+b
            else:
                w+=b
                ans=ans+(w-a)

        return ans/len(customers)
        