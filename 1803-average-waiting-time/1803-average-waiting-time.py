class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
       
        w=0
        ans=0
        for a,b in customers:
            w =  max(w, a) + b
            ans += (w - a)

        return ans/len(customers)
        