class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        mp = {}
        for a, b in edges:
            if a not in mp:
                mp[a]=[]
            if b not in mp:
                mp[b]=[]
            mp[a].append(b)
            mp[b].append(a)
        
        stack = [start]
        seen = set()
        
        while stack: 
            node = stack.pop() 
            if node == end:
                return True 
            if node in seen:
                continue
            seen.add(node) 
            for neighbor in mp[node]:
                stack.append(neighbor) 
        return False