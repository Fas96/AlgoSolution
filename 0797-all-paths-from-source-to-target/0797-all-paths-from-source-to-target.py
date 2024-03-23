class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        T = len(graph)-1
        S, ans = [([], 0)], []

        while S : 
            path, cur = S.pop()  
            if cur == T :
                ans.append((path + [T]))
            else : 
                for n in graph[cur] : 
                    S.append((path + [cur], n))

        return ans