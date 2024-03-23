class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        stack, ans = [([], 0)], []

        while stack : 
            path, node = stack.pop()  
            if node == target :
                ans.append((path + [target]))
            else : 
                for n in graph[node] : 
                    stack.append((path + [node], n))

        return ans