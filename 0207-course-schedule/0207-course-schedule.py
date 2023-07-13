
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for x, y in prerequisites: g[x].append(y)
        canFinishAt = [0]*numCourses
         
        def dfs(idx):
            if canFinishAt[idx] == -1:
                return False
            if canFinishAt[idx] == 1:
                return True
            canFinishAt[idx] = -1
            for nei in g[idx]:
                if not dfs(nei):
                    return False
            canFinishAt[idx] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        