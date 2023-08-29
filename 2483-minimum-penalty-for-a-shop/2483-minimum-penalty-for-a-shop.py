class Solution:
    def bestClosingTime(self, customers: str) -> int:
         
        if 'N' not in customers:return len(customers)
        if 'Y' not in customers:return 0
        
        penalty=0
        mx=0
        minPenal=-1
        for i in range(len(customers)):
            penalty += 1 if customers[i] == 'Y' else -1
            if penalty > mx:
                mx=penalty
                minPenal=i
        return minPenal+1
                
            
        