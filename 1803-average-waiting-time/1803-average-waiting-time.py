class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        w=ans=0
        for a,b in c:
            w =  max(w, a) + b
            ans += (w - a)
        return ans/len(c)
        