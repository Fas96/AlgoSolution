class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]: 
        N = len(graph)
        safe={}
        def findSafe(idx):
            if idx in safe:
                return safe[idx]
            safe[idx]=False
            for neighboor in graph[idx]:
                if not findSafe(neighboor):
                    return safe[idx]
            safe[idx]=True
            return True
            
        return [i for i in range(N) if findSafe(i) ]