class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        roots=list(range(n+1))
        def find(x):
            if x!=roots[x]:
                roots[x]=find(roots[x])
            return roots[x]
        def union(x,y):
            r1=find(x)
            r2=find(y)
            if r1!=r2:
                roots[r2]=r1
                return True
            return False
        edges=[]
        for u,v,c in pipes:
            edges.append((c,u-1,v-1))
        for i,v in enumerate(wells):
            edges.append((v,i,n))
        edges.sort()
        ans=0
        for c,u,v in edges:
            if union(u,v):
                ans+=c
        return ans