class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mp=[0]*n
        roadsSet = set()

        for u,v in roads:
            mp[u] += 1
            mp[v] += 1
            roadsSet.add((min(u,v),max(u,v)))
        rank=0
        for i in range(n):
            for j in range(i+1,n):
                if (i,j) in roadsSet:
                    rank=max(rank,mp[i]+mp[j]-1)
                else:
                    rank=max(rank,mp[i]+mp[j])
        return rank
        