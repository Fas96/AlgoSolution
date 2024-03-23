class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        T=len(graph)-1
        S=[([],0)]
        ans=[]
        while S:
            p,c=S.pop()
            if c==T:
                ans.append(p+[T])
            else:
                for n in graph[c]:
                    S.append((p+[c],n))
                
        return ans