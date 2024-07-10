class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec=[]
        for o in operations:
            if o=='+':
                rec.append(rec[-1]+rec[-2])
            elif o=='D':
                rec.append(rec[-1]*2)
            elif o=='C':
                rec=rec[:len(rec)-1]
            else:
                rec.append(int(o))
   
        return sum(rec)
        