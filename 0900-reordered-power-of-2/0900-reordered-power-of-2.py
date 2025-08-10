class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        p2=[]
        for i in range(31):
            p2.append(2**i)

        N,fn=len(str(n)),Counter(str(n)) 
        fp=defaultdict(int)
        p=[]
        for pp in p2:
            if len(str(pp))==N:
                p.append(pp)
        for c in p:
            cc=Counter(str(c)) 
            if cc==fn:
                return True
        return False 
        