class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        rs=sum(rolls)
    
        fd=((m+n)*mean-rs)//n 
        
        ms = ((m+n)*mean) - rs
        if ms < n or ms > n * 6: return []
        
        addUp=[1]*n 
        ms-=n
        for i in range(n): 
            addUp[i] += min(5, ms) 
            ms -= 5 
            if ms <= 0: break 
        return addUp