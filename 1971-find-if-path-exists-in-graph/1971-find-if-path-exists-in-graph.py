class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mp=defaultdict(list)
        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)
        q=collections.deque([source])
        vst=set()
        while q:
            cur=q.popleft()
            if cur==destination:
                return True
            
            for n in mp[cur]:
                if n in vst:
                    continue
                vst.add(n)
                q.append(n)
        return False
                    
            