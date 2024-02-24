class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        se=set([0,firstPerson])
        tm={}
        for s,d,t in meetings:
            if t not in tm:
                tm[t]=defaultdict(list)
            tm[t][s].append(d)
            tm[t][d].append(s)
            
        def dfs(src,adj):
            if src in vsted:
                return
            vsted.add(src)
            se.add(src)
            for n in adj[src]:
                dfs(n,adj)
            
        
        
        for t in sorted(tm.keys()):
            vsted=set()
            for src in tm[t]:
                if src in se:
                    dfs(src,tm[t])
        return list(se)

        