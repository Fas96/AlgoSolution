class UF:
    def __init__(self, size):
        self.root=[i for i in range(size)]
        self.rank=[float("-inf")]*(size)
        self.count=size
    def find(self,x):
        if x==self.root[x]:    
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootX,rootY=self.find(x),self.find(y)
        if rootX==rootY:
            return
        if self.rank[rootX]>self.rank[rootY]:
            self.root[rootY]=self.root[rootX]
        elif self.rank[rootX]<self.rank[rootY]:
            self.root[rootX]=self.root[rootY]
        else:
            self.root[rootX]=self.root[rootY]
            self.rank[rootY]+=1
        self.count -= 1
        
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    def getCount(self):
        return self.count
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UF(n)       
        data = sorted(logs, key = lambda x: x[0])
        for time, n1, n2 in data:
            uf.union(n1, n2)
            if uf.getCount() == 1:
                return time    
        return -1 
        