class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={cu:[] for cu in range(numCourses)}
        for c,p in prerequisites:
            mp[c].append(p)
        v=set()
        @cache
        def dfs(cur):
            if cur in v: return False
            if mp[cur]==[]:return True
            v.add(cur)
            for n in mp[cur]:
                if not dfs(n):return False
            v.remove(cur)
            mp[cur]==[]
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True
        