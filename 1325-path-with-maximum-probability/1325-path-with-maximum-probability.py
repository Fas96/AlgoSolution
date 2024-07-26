class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        mp=defaultdict(list) 
        for [t,f],p in zip(edges,succProb):
            mp[t].append((f,p))
            mp[f].append((t,p)) 
        def djk(node): 
            prq=[(-1,node)]
            visited = set()
            while prq:
                cp,curNode=heapq.heappop(prq) 
                if curNode==end_node:  return -cp
                if curNode in visited: continue
                visited.add(curNode) 
                for neighbor,prob in mp[curNode]:
                    heapq.heappush(prq,(cp*prob,neighbor))
            return 0
         
        return djk(start_node)

        