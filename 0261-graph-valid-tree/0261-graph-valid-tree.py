class UF:
    def __init__(self, size):
        self.root=list(range(size))
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)==0 and n>1:
            return False
        uf=UF(n)
        x=len(edges)
     
        num_trees = n
        for a, b in edges: 
            parent_a, parent_b = uf.find(a), uf.find(b) 
            if parent_a == parent_b:
                return False 
            num_trees -= 1
            uf.union(parent_a, parent_b) 
        return num_trees == 1
    
        