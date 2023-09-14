class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g=defaultdict(list)
         
        for s,d in sorted(tickets, reverse=True):
            g[s].append(d)
        seen=[] 
        def dfs(loc):
            while g[loc]:
                dfs(g[loc].pop())
            seen.append(loc)
        
        dfs("JFK")
        return seen[::-1]
        