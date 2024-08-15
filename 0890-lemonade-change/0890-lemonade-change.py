class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t=0,0
        for b in bills: 
            if b==5: f+=1
            elif b==10:
                f-=1
                t+=1
            elif t>0:
                f-=1
                t-=1
            else: f-=3
            if f<0: return False
        return True
        
        return True
        