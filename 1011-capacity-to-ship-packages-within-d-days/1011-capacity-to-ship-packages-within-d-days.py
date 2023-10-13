class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canGetAllDays(w,d,randN):
            t=0
            ud=1
            for ew in w:
                t+=ew
                if t>randN:
                    t=ew
                    ud+=1
            return ud<=d
        L=max(weights)
        R=sum(weights)
        while L<=R:
            M=(L+R)//2
            if(canGetAllDays(weights,days, M)):
                R=M-1
            else:
                L=M+1
        return L
        