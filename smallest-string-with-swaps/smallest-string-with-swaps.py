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
        if rootX>rootY:
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UF(n)
        for x, y in pairs:
            uf.union(x, y)
        
        alias = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            alias[root].append(s[i])
        for i in alias:
            alias[i].sort(reverse=True)
                
        res = []
        for i in range(n):
            res.append(alias[uf.find(i)].pop())
        
        return ''.join(res) 
        
        