class Solution(object):
    def validPath(self, n, edges, source, destination):
        d = {i: [] for i in range(n)}
       
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        seen = set()

        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            seen.add(node)
            for n in d[node]:
                if dfs(n, end, seen):
                    return True
            return False

        return dfs(source, destination, seen)