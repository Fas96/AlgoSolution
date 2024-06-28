class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        g=[0]*n
        for x in roads:
            g[x[0]]+=1;g[x[1]]+=1;
        g.sort()
        ans=0
        for i in range(n):
            ans+=((i+1)*g[i])
        return ans