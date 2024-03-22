class UF:
    def __init__(self, size):
        self.root=[i for i in range(size)]
        self.rank=[1]*(size)
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected)==0:
            return 0
        n=len(isConnected)
        uf=UF(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j) 
        return uf.getCount()
            
                    

                    
                    