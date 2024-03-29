class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp={cu:[] for cu in range(numCourses)}
        for c,p in prerequisites:
            mp[c].append(p)
        v,c=set(),set()
        
        @cache
        def dfs(cur):
            if cur in c: return False
            if cur in v: return True  
            c.add(cur)
            for n in mp[cur]:
                if not dfs(n):return False
            c.remove(cur)
            v.add(cur) 
            ans.append(cur)
            return True
        ans=[]
        for i in range(numCourses):
            if not dfs(i): return []
        return ans
        