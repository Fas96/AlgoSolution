class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        mp=defaultdict(list)

        idx=0
        for t,f in edges:
            mp[t].append((f,succProb[idx]))
            mp[f].append((t,succProb[idx]))
            idx+=1
        def djk(node):
             
            prq=[(-1,node)]
            visited = set()
            while prq:
                curDistance,curNode=heapq.heappop(prq) 
                if curNode==end_node:  return -curDistance
                if curNode in visited: continue
                visited.add(curNode) 
                for neighbor,prob in mp[curNode]:
                    heapq.heappush(prq,(curDistance*prob,neighbor))
            return 0
         
        return djk(start_node)

        