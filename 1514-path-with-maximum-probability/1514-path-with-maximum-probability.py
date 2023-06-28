class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if start == end: 
            return 0
        
        G = collections.defaultdict(list)
        
        for i,[a,b] in enumerate(edges):
            G[a].append((b,succProb[i]))
            G[b].append((a,succProb[i]))
        
        prob = [0 for _ in range(n)]
        
        prob[start] = 0
        
        PQ = [(-1,start)]
        
        while(PQ):
            currProb, node = heapq.heappop(PQ)
            
            currProb *= -1
            
            if prob[node] > currProb: continue
            
            if node == end: return currProb
            
            for (nbr,nextProb) in G[node]:
                if nextProb *currProb > prob[nbr]:
                    heapq.heappush(PQ,(-currProb*nextProb, nbr))
                    prob[nbr] = currProb*nextProb
    
        return 0
        
        
        