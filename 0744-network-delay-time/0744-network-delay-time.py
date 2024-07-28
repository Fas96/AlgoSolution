class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp=defaultdict(list)
        for ui, vi, wi in times:
            mp[ui].append((wi,vi))
        vs=set()
        pq=[(0,k)]
        while pq:
            curTime,curNode=heappop(pq)
            vs.add(curNode)
            if len(vs)==n:return curTime
            for tt,neighbor in mp[curNode]:
                if neighbor not in vs:
                    heappush(pq,(curTime+tt,neighbor))
            
        return -1